# coding:utf-8
import unittest, math, sys, os, logging
filepath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(filepath)
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
        fly_direction,
        application='unknown',):
    # 判断输入是否合法
    if aerocraft not in aerocrafts:
        return False, '未知的飞机类型: %s' % str(aerocraft)
    aerocraft_attributes = aerocrafts[aerocraft]
    if camera not in cameras:
        return False, '未知的载荷类型: %s' % str(aerocraft)
    camera_attributes = cameras[camera]
    try:
        ground_resolution_m = float(ground_resolution_m)
    except:
        return False, '地表分辨率必须是数字'
    try:
        sideway_overlap = float(sideway_overlap)
        assert sideway_overlap >= 0. and sideway_overlap < 1.
        if 'sar' not in camera_attributes['type']:
            forward_overlap = float(forward_overlap)
            assert forward_overlap >= 0. and forward_overlap < 1.
    except Exception as e:
        logging.exception(e)
        return False, '重叠度必须是数字,且在[0,1)'
    
    # 确定路径规划的参数
    fly_height = None
    shoot_mode = 'sar' if 'sar' in camera_attributes['type'] else 'shutter'
    side_photo_ground_meters = None
    forward_shooting_space_meters = None
    forward_photo_ground_meters = None
    fly_position_left_offset_meters = 0.
    if 'sar' in camera_attributes['type']:
        # 计算飞行高度
        R_m = camera_attributes['R_suggest_m']
        look_angle_degrees = camera_attributes['right_look_angle_degrees']
        if look_angle_degrees < 0:
            look_angle_degrees = -look_angle_degrees
        range_beam_width_degrees = camera_attributes['range_beam_width_degrees']
        fly_height = R_m * math.cos(look_angle_degrees)
        if fly_height > aerocraft_attributes['max_height_m']:
            return False, '飞行高度过高, 请调整Sar安装角'
        if fly_height < aerocraft_attributes['min_height_m']:
            return False, '飞行高度过低, 请调整Sar安装角'

        # 地面相片大小
        near_range_m = R_m / math.cos(look_angle_degrees - range_beam_width_degrees/2)
        far_range_m = R_m / math.cos(look_angle_degrees + range_beam_width_degrees/2)
        side_photo_ground_meters = far_range_m - near_range_m
        side_shooting_space_meters = side_photo_ground_meters*(1-sideway_overlap)

        fly_position_left_offset_meters = (far_range_m + near_range_m) / 2.
        if camera_attributes['right_look_angle_degrees'] < 0:  # 如果Sar向左看
            fly_position_left_offset_meters = -fly_position_left_offset_meters
    else:
        # 计算飞行高度
        min_fly_height = camera_attributes['f_m']/camera_attributes['pixel_size_m'] *ground_resolution_m
        fly_height = min_fly_height
        if fly_height > aerocraft_attributes['max_height_m']:
            fly_height = aerocraft_attributes['max_height_m']
            ground_resolution_m = camera_attributes['pixel_size_m']*fly_height/ camera_attributes['f_m']
        if fly_height < aerocraft_attributes['min_height_m']:
            return False, '飞行高度过低, 请调大地面分辨率'

        # 计算地面相片大小与拍摄间隔
        side_photo_ground_meters = camera_attributes['pixel_num_x'] *   ground_resolution_m
        forward_photo_ground_meters = camera_attributes['pixel_num_y'] *    ground_resolution_m
        forward_shooting_space_meters = forward_photo_ground_meters*    (1-forward_overlap)
        side_shooting_space_meters = side_photo_ground_meters*(1-sideway_overlap)
    
    # 航迹规划
    fly_route, photo_ground_rectangles_geo, debug_info = route_planning(
        shooting_area=area_points_list,
        shooting_area_coor_egsp_code='4326',
        fly_direction=fly_direction,
        forward_shooting_space_meters=forward_shooting_space_meters,
        side_shooting_space_meters=side_shooting_space_meters,
        forward_photo_ground_meters=forward_photo_ground_meters,
        side_photo_ground_meters=side_photo_ground_meters,
        fly_height_m=fly_height,
        shoot_mode=shoot_mode,
        fly_position_left_offset_meters=fly_position_left_offset_meters,
    )

    # 返回结果
    res = {
        # 重要信息
        'name': mission_name,
        'shoot_mode': 'shutter',
        'route_coors': fly_route, # 航点
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
            print(mission_attributes)
            succ, res = mission_planning(
                area_points_list=aera,
                mission_name=mission_name,
                aerocraft=mission_attributes['aerocraft'],
                camera=mission_attributes['cameras'],
                ground_resolution_m=mission_attributes['ground_resolution_m'],
                forward_overlap=mission_attributes['forward_overlap'],
                sideway_overlap=mission_attributes['sideway_overlap'],
                fly_direction=mission_attributes['fly_direction'],
                application=mission_attributes['application'],
            )
            if succ:
                print (succ)
            else:
                print (res)


if __name__ == '__main__':
    unittest.main()
