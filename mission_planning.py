# coding:utf-8
import unittest
from camera import cameras
from aerocraft import aerocrafts
from route_planning import route_planning

def mission_planning(
        area_points_list,
        mission_name,
        aerocraft,
        camera,
        ground_resolution_m,
        forward_overlap,
        sideway_overlap,
        fly_east_west_direction,
        application='unknown',):
    
    if aerocraft not in aerocrafts:
        return False, '未知的飞机类型: %s' % str(aerocraft)
    aerocraft_attributes = aerocrafts[aerocraft]

    if camera not in cameras:
        return False, '未知的载荷类型: %s' % str(aerocraft)
    camera_attributes = cameras[camera]
    
    # 确定航高
    min_fly_height = camera_attributes['f_m']/camera_attributes['pixel_size_m']*ground_resolution_m
    fly_height = min_fly_height
    if fly_height > aerocraft_attributes['max_height_m']:
        fly_height = aerocraft_attributes['max_height_m']
        ground_resolution_m = camera_attributes['pixel_size_m']*fly_height/camera_attributes['f_m']
    if fly_height < aerocraft_attributes['min_height_m']:
        return False, '飞行高度过低, 请调大地面分辨率'

    # 计算地面相片大小与拍摄间隔
    side_photo_ground_meters = camera_attributes['pixel_num_x'] * ground_resolution_m
    forward_photo_ground_meters = camera_attributes['pixel_num_y'] * ground_resolution_m
    forward_shooting_space_meters = forward_photo_ground_meters*(1-forward_overlap)
    side_photo_ground_meters = side_photo_ground_meters*(1-sideway_overlap)

    # 确定飞行方向
    fly_direction = None
    if fly_east_west_direction:
        fly_direction = (1, 0)
    else:
        return False, 'TODO: 待完成根据拍摄区域自适应获得飞行方向功能'
    
    # 航迹规划
    shoot_coors_geo, photo_ground_rectangles_geo, debug_info = route_planning(
        shooting_area=area_points_list,
        shooting_area_coor_egsp_code='4326',
        fly_direction=fly_direction,
        forward_shooting_space_meters=forward_shooting_space_meters,
        side_shooting_space_meters=side_photo_ground_meters,
        forward_photo_ground_meters=forward_photo_ground_meters,
        side_photo_ground_meters=side_photo_ground_meters,
    )

    # 返回结果
    res = {
        'shoot_coors_geo': shoot_coors_geo, # 拍摄点坐标
        'photo_ground_rectangles_geo': photo_ground_rectangles_geo, # 拍摄得到图像在地面上的投影
        'fly_height': fly_height, # 航高
        'aerocraft': aerocraft_attributes, # 飞机与属性
        'camera': camera_attributes, # 载荷与属性
    }
    return True, res


class _UnitTest(unittest.TestCase):
    def test_missions(self):
        from preload_missions import missions
        aera = [(30, 30), (30, 30.1), (30.1, 30.1), (30.1, 30)]
        for mission_name in missions:
            mission_attributes = missions[mission_name]
            succ, res = mission_planning(
                area_points_list=aera,
                mission_name=mission_name,
                aerocraft=mission_attributes['aerocraft'],
                camera=mission_attributes['cameras'],
                ground_resolution_m=mission_attributes['ground_resolution_m'],
                forward_overlap=mission_attributes['forward_overlap'],
                sideway_overlap=mission_attributes['sideway_overlap'],
                fly_east_west_direction=mission_attributes['fly_east_west_direction'],
                application=mission_attributes['application'],
            )
            if succ:
                print (succ)
            else:
                print (res)


if __name__ == '__main__':
    unittest.main()
