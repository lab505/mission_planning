# coding:utf-8
import unittest
from .camera import cameras
from .aerocraft import aerocrafts
from .route_planning import route_planning

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
    # 判断输入是否合法
    try:
        ground_resolution_m = float(ground_resolution_m)
    except:
        return False, '地表分辨率必须是数字'
    try:
        forward_overlap = float(forward_overlap)
        sideway_overlap = float(sideway_overlap)
        assert forward_overlap >= 0. and forward_overlap < 1.
        assert sideway_overlap >= 0. and sideway_overlap < 1.
    except:
        return False, '重叠度必须是数字,且在[0,1)'
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

    shoot_mode = 'shutter'
    route_coors = None
    if shoot_mode == 'shutter':
        route_coors = [{'gps': (x,y), 'control_code': 'shutter'} for x, y in shoot_coors_geo]
    else:
        route_coors = []
        for i in range(len(shoot_coors_geo)):
            x, y = shoot_coors_geo
            if i % 2 == 0:
                control_code = 'on'
            else:
                control_code = 'off'
            route_coors.append({'gps': (x, y), 'control_code': control_code})
    # 返回结果
    res = {
        # 重要信息
        'name': mission_name,
        'shoot_mode': 'shutter',
        'route_coors': route_coors, # 航点
        'fly_height_m': fly_height, # 航高
        'aerocraft': aerocraft_attributes, # 飞机与属性
        'camera': camera_attributes, # 载荷与属性

        # 其它信息
        'mission_area': area_points_list,
        'application': application, # 所属应用(生态/洪涝/反恐)
        'forward_overlap': forward_overlap,
        'sideway_overlap': sideway_overlap,
        'ground_resolution_m': ground_resolution_m,
        'photo_ground_rectangles_geo': photo_ground_rectangles_geo, # 拍摄得到图像在地面上的投影
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
