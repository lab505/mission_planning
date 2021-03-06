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
        fly_direction_degree,
        aerocraft_num,
        application,
        board_region,
        board_region_max_fly_height_m,
        right_look_angle_degrees,
        R_suggest_m,
        f_m,
        bend_radius,
):
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
        aerocraft_num = int(aerocraft_num)
        assert aerocraft_num > -1
    except:
        return False, '飞机数量必须是0或正整数'
    try:
        fly_direction = float(fly_direction_degree)
        fly_direction_r = fly_direction / 180. * math.pi
        fly_direction_x = math.cos(fly_direction_r)
        fly_direction_y = math.sin(fly_direction_r)
        fly_direction = (fly_direction_x, fly_direction_y)
    except:
        return False, '飞行方向必须是数字'
    try:
        sideway_overlap = float(sideway_overlap)
        assert sideway_overlap >= 0. and sideway_overlap < 1.
        if camera_attributes['type'] == 'camera':
            forward_overlap = float(forward_overlap)
            assert forward_overlap >= 0. and forward_overlap < 1.
        else:
            forward_overlap = None
    except Exception as e:
        logging.exception(e)
        return False, '重叠度必须是数字,且在[0,1)'
    print('ok')
    # 确定路径规划的参数
    fly_height = None
    shoot_mode = {
        'sar': 'sar',
        'camera': 'shutter',
        'video': 'video',
    }[camera_attributes['type']]
    side_photo_ground_meters = None
    forward_shooting_space_meters = None
    forward_photo_ground_meters = None
    fly_position_left_offset_meters = 0.

    max_fly_height_m = aerocraft_attributes['max_height_m']
    min_fly_height_m = aerocraft_attributes['min_height_m']
    if board_region_max_fly_height_m > max_fly_height_m:
        max_fly_height_m = board_region_max_fly_height_m

    calculate_fly_height = None
    actually_ground_resolution_m = None
    look_angle_degrees=None
    if 'sar' in camera_attributes['type']:
        # 计算飞行高度
        look_angle_degrees = right_look_angle_degrees
        if look_angle_degrees < 0:
            look_angle_degrees = -look_angle_degrees
        range_beam_width_degrees = camera_attributes['range_beam_width_degrees']
        camera_suggest_fly_height = R_suggest_m * math.cos(math.pi / 180. * look_angle_degrees)
        calculate_fly_height = camera_suggest_fly_height
        camera_max_fly_height = camera_attributes['R_max_m'] * math.cos(math.pi / 180. * look_angle_degrees)
        camera_min_fly_height = camera_attributes['R_min_m'] * math.cos(math.pi / 180. * look_angle_degrees)
        if camera_min_fly_height > max_fly_height_m:
            return False, 'Sar允许的最小飞行高度%f(m) 超出 飞机、空域允许的最大飞行高度%f(m)，请调整' % (camera_min_fly_height, max_fly_height_m)
        if camera_max_fly_height < min_fly_height_m:
            return False, 'Sar允许的最大飞行高度%f(m) 不足 飞机允许的最小飞行高度%f(m)，请调整' % (camera_max_fly_height, min_fly_height_m)
        max_fly_height_m = min(camera_max_fly_height, max_fly_height_m)
        min_fly_height_m = max(camera_min_fly_height, min_fly_height_m)

        if camera_suggest_fly_height > max_fly_height_m and camera_suggest_fly_height >= min_fly_height_m:
            fly_height = max_fly_height_m
        elif camera_suggest_fly_height < min_fly_height_m:
            fly_height = min_fly_height_m
        else:
            fly_height = camera_suggest_fly_height

        # 地面相片大小
        near_range_m = fly_height / math.cos(math.pi / 180. * (look_angle_degrees - range_beam_width_degrees / 2))
        far_range_m = fly_height / math.cos(math.pi / 180. * (look_angle_degrees + range_beam_width_degrees / 2))
        side_photo_ground_meters = far_range_m - near_range_m
        side_shooting_space_meters = side_photo_ground_meters * (1 - sideway_overlap)

        fly_position_left_offset_meters = (far_range_m + near_range_m) / 2.
        if right_look_angle_degrees< 0:  # 如果Sar向左看
            fly_position_left_offset_meters = -fly_position_left_offset_meters
    else:
        # 计算飞行高度
        calculate_fly_height = camera_max_fly_height = f_m / camera_attributes['pixel_size_m'] * ground_resolution_m
        fly_height = camera_max_fly_height
        if camera_max_fly_height < min_fly_height_m:
            return False, '分辨率允许的最大飞行高度%f(m) 不足 飞机的最小飞行高度%f(m)，请调整' % (camera_max_fly_height, min_fly_height_m)
        if camera_max_fly_height < max_fly_height_m:
            fly_height = camera_max_fly_height
        else:
            fly_height = max_fly_height_m
        actually_ground_resolution_m = camera_attributes['pixel_size_m'] / f_m * fly_height

        # 计算地面相片大小与拍摄间隔
        side_photo_ground_meters = camera_attributes['pixel_num_x'] * actually_ground_resolution_m
        side_shooting_space_meters = side_photo_ground_meters * (1 - sideway_overlap)
        forward_photo_ground_meters = forward_shooting_space_meters = None
        if camera_attributes['type'] == 'camera':
            forward_photo_ground_meters = camera_attributes['pixel_num_y'] * actually_ground_resolution_m
            forward_shooting_space_meters = forward_photo_ground_meters * (1 - forward_overlap)

    # 航迹规划
    lines, photo_ground_rectangles_geo, debug_info = route_planning(
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

    totle_length_m = 0.
    for line in lines:
        totle_length_m += line['length']
    max_mileage_m = aerocraft_attributes['max_mileage_km'] * 1000.

    need_aerocraft_num = None
    if aerocraft_num == 0:
        need_aerocraft_num = math.ceil(totle_length_m / max_mileage_m)
    else:
        need_aerocraft_num = aerocraft_num
    ave_mileage_m = totle_length_m / need_aerocraft_num

    # if aerocraft_num != 0 and need_aerocraft_num > aerocraft_num:
    #    return None, '需要%d架飞机, 只有%d架, 请重新调整任务'
    i_line = 0
    aerocraft_lines = []
    for i_plane in range(need_aerocraft_num):
        plane_length_m = 0.
        plane_line_num = 0
        one_aerocraft_fly_points = []
        while plane_length_m < ave_mileage_m and i_line < len(lines):
            one_aerocraft_fly_points.extend(lines[i_line]['points'])
            plane_length_m += lines[i_line]['length']
            plane_line_num += 1
            i_line += 1
        if len(one_aerocraft_fly_points) > 0:
            aerocraft_lines.append({
                'fly_points': one_aerocraft_fly_points,
                'plane_line_num': plane_line_num,
                'length_m': plane_length_m,
            })

    if board_region == None:
        board_region = debug_info['board_region']
    # 返回结果
    res = []
    for i in range(len(aerocraft_lines)):  # 对于每架飞机
        fly_route = aerocraft_lines[i]['fly_points']
        length_m = aerocraft_lines[i]['length_m']
        line_num = aerocraft_lines[i]['plane_line_num']
        res.append({
            # 重要信息
            'bend_radius':bend_radius,
            'mission_num': i + 1,
            'mission_name': mission_name,
            'mission_aerocraft_id':aerocraft_attributes['fly_control_num'] ,
            'shoot_mode': 'shutter',
            'route_coors': fly_route,  # 航点
            'length_m': length_m,  # 距离
            'fly_height_m': fly_height,  # 航高
            'plane': aerocraft_attributes,  # 飞机与属性
            'camera': camera_attributes,  # 载荷与属性
            'board_region': board_region,  # 可飞行区域
            'line_num': line_num,  # 航线数量
            'calculate_fly_height': calculate_fly_height,  # 根据相机要求计算出的航高
            'actually_ground_resolution_m': actually_ground_resolution_m,  # 实际拍出的地面分辨率
            'look_angle_degrees':look_angle_degrees,
            # 'fly_direction': fly_direction_degree,
      
            # 其它信息
            'mission_area': area_points_list,
            'application': application,  # 所属应用(生态/洪涝/反恐)
            'forward_overlap': forward_overlap,
            'sideway_overlap': sideway_overlap,
            'ground_resolution_m': ground_resolution_m,
            'photo_ground_rectangles_geo': photo_ground_rectangles_geo,  # 拍摄得到图像  在地面上的投影
        })
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
                aerocraft_num=5,
            )
            if succ:
                print(succ)
            else:
                print(res)


if __name__ == '__main__':
    unittest.main()
