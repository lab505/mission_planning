# coding:utf-8
import unittest, math
import osgeo.ogr
import numpy as np


# 是否顺时针记录多边形
POLYGON_AS_CLOCKWISE = True


def get_meters_between_2_gps_points(lon_1, lat_1, lon_2, lat_2):
    from geographiclib.geodesic import Geodesic  # pip install geographiclib
    return Geodesic.WGS84.Inverse(lat_1, lon_1, lat_2, lon_2)['s12']


def get_meters_between_2points(x_1, y_1, x_2, y_2, epsgcode):
    if epsgcode is '4326':
        return get_meters_between_2_gps_points(x_1, y_1, x_2, y_2)
    else:
        raise 'TODO: change coor to wgs84 gps'


def calculate_x_y_ground_meters(min_x, min_y, max_x, max_y, center_x, center_y, epsgcode):
    meters_per_x = get_meters_between_2points(
        max_x, center_y, min_x, center_y, epsgcode)/(max_x-min_x)
    meters_per_y = get_meters_between_2points(
        center_x, max_y, center_x, min_y, epsgcode)/(max_y-min_y)
    return meters_per_x, meters_per_y


def get_direction_angel(x, y):
    direction_angel = np.pi/2
    if abs(x) > 0.000001:
        direction_angel = np.arctan(y/x)
    if y < 0.:
        direction_angel += np.pi
    return direction_angel


def get_bounding_box(points_list):
    nparray = np.array(points_list, dtype=float)
    assert len(nparray.shape) == 2 and nparray.shape[1] == 2
    min_x, max_x = np.min(nparray[:, 0]), np.max(nparray[:, 0])
    min_y, max_y = np.min(nparray[:, 1]), np.max(nparray[:, 1])
    return min_x, min_y, max_x, max_y


def get_coor_trans_mat(polygon_list, epsgcode, fly_direction):
    '''
    获取一个依据拍摄区域(polygon_list)和飞行方向(fly_direction)产生的坐标转换, 可将目标区域转换至拍摄坐标
    拍摄坐标系产生规则:转换后的坐标系的x轴指向飞行方向, 单位刻度为米, 坐标原点为拍摄区域外包矩形的中心, 以外包矩形内的平均地面分辨率均匀拉伸
    本函数返回值:转换矩阵(地理坐标系to拍摄坐标)和逆转换矩阵(拍摄坐标to地理坐标)
    '''
    min_x, min_y, max_x, max_y = get_bounding_box(polygon_list)
    center_x, center_y = (min_x+max_x)/2., (min_y+max_y)/2.
    meters_per_x, meters_per_y = calculate_x_y_ground_meters(min_x, min_y, max_x, max_y, center_x, center_y, epsgcode)

    # move to origin
    # newx = x-center_x, same to y
    trans_1 = np.array([
        [1., 0., -center_x],
        [0., 1., -center_y],
        [0., 0., 1.],
    ], dtype=float)

    # scale_to_meters
    # newx = x*meters_per_x, same to y
    # fly_direction_meters_x = fly_direction_x*meters_per_x, same to y
    trans_2 = np.array([
        [meters_per_x, 0., 0.],
        [0., meters_per_y, 0.],
        [0.,           0., 1.],
    ], dtype=float)

    fly_direction_meters_x = fly_direction[0] * meters_per_x
    fly_direction_meters_y = fly_direction[1] * meters_per_y

    # rotate_to_fly_direction
    # new_x = xcos(a)+ysin(a)
    # new_y =-xsin(a)+ycos(a)
    a = get_direction_angel(fly_direction_meters_x, fly_direction_meters_y)
    trans_3 = np.array([
        [np.cos(a),  np.sin(a), 0.],
        [-np.sin(a), np.cos(a), 0.],
        [0.,     0.,            1.],
    ], dtype=float)

    # trans3*trans2*trans1*old_coor = new_coor
    trans_mat = np.dot(np.dot(trans_3, trans_2), trans_1)
    inv_trans_mat = np.linalg.inv(trans_mat)

    return trans_mat, inv_trans_mat


def one_point_coor_trans(x, y, np_trans_mat):
    ori_coor = np.array([[x], [y], [1]], dtype=float)
    new_coor = np.dot(np_trans_mat, ori_coor)
    return new_coor[0][0]/new_coor[2][0], new_coor[1][0]/new_coor[2][0]


def coor_trans(points_list, np_trans_mat):
    return [one_point_coor_trans(x, y, np_trans_mat) for x, y in points_list]

def get_structured_board_region(board_region_area):
    board_region = []
    for i in range(len(board_region_area)):
        board_region.append({
            'number': i+1,
            'longitude': board_region_area[i][0],
            'latitude': board_region_area[i][1],
        })
    return board_region

def points_to_gdal_polygon(points_list):
    ring = osgeo.ogr.Geometry(osgeo.ogr.wkbLinearRing)
    for x, y in points_list:
        ring.AddPoint(x, y)
    if not points_list[-1] == points_list[0]:
        ring.AddPoint(points_list[0][0], points_list[0][1])
    poly = osgeo.ogr.Geometry(osgeo.ogr.wkbPolygon)
    poly.AddGeometry(ring)
    return poly

# TODO 用高斯坐标系
# TODO 问题 地表不平
# TODO 拍摄区域buffer
# TOTHINK 凹多边形
# TODO 航点ID
# TODO 火星坐标 交给地理所
# TODO 输出格式 飞控多用kml
def route_planning(shooting_area,
                   shooting_area_coor_egsp_code,
                   fly_direction,  # 飞行方向
                   forward_shooting_space_meters,  # 航向拍摄间隔(米)
                   side_shooting_space_meters,  # 旁向拍摄间隔(米)
                   forward_photo_ground_meters,  # 拍摄相片投影到地面上的大小
                   side_photo_ground_meters,
                   fly_height_m,
                   shoot_mode,  # shutter/sar
                   fly_position_left_offset_meters,  # 如果Sar向右拍摄,则该值为正
                   #aerocraft_num,  # 飞机数量
                   board_area_buffer_m=5000,
                   ):
    '''
    航迹规划
    '''
    trans_mat, inv_trans_mat = get_coor_trans_mat(shooting_area, shooting_area_coor_egsp_code, fly_direction)
    shooting_area_transed = coor_trans(shooting_area, trans_mat)
    min_x, min_y, max_x, max_y = get_bounding_box(shooting_area_transed)
    area_gdal_polygon = points_to_gdal_polygon(shooting_area_transed)
    photo_size_ground_meters_half_y = side_photo_ground_meters/2.
    if shoot_mode != 'sar':
        photo_size_ground_meters_half_x = forward_photo_ground_meters/2.
    
    # 获取buffer
    board_area = area_gdal_polygon.Buffer(distance=board_area_buffer_m)
    board_area_geometry = board_area.GetGeometryRef(0)
    board_area_points = []
    for i in range(0, board_area_geometry.GetPointCount()):
        pt = board_area_geometry.GetPoint(i)
        board_area_points.append((pt[0], pt[1]))
    board_area_points_geo = coor_trans(board_area_points, inv_trans_mat)
    board_area_res = get_structured_board_region(board_area_points_geo)

    # 确定航线数量与位置(lines_num lines_y)
    area_height = max_y-min_y
    lines_num = math.ceil(area_height/side_shooting_space_meters)+1
    lines_y = [side_shooting_space_meters * (i-(lines_num-1)/2.) for i in range(lines_num)]
    if shoot_mode == 'sar':
        lines_num = math.ceil(area_height/side_shooting_space_meters*2.)+1
        if (lines_num % 2) == 0:
            lines_num = lines_num + 1
        else:
            lines_num = lines_num
        lines_y = [side_shooting_space_meters/2. * (i-(lines_num-1)/2.) for i in range(lines_num)]
    #aerocraft_lines_id = [[] for i_aerocraft in range(aerocraft_num)]
    #ave_lines = lines_num // aerocraft_num
    #_i_line = 0
    #for i_aerocraft in range(aerocraft_num):
    #    for _ in range(ave_lines):
    #        aerocraft_lines_id[i_aerocraft].append(_i_line)
    #        _i_line += 1
    #while _i_line < lines_num:
    #    aerocraft_lines_id[-1].append(_i_line)
    #    _i_line += 1

    photo_ground_rectangles = []
    photo_ground_rectangles_geo = []

    fly_right = True
    lines = []
    for line_y in lines_y:
        # 计算条带宽度
        line_min_y, line_max_y = line_y - side_shooting_space_meters/2., line_y     + side_shooting_space_meters/2.

        # 计算条带多边形(line_polygon)及其外包矩形(line_polygon_envelope)
        line_rectangle = [
            (min_x, line_min_y), (min_x, line_max_y), (max_x, line_max_y),  (max_x, line_min_y)]
        if not POLYGON_AS_CLOCKWISE:
            line_rectangle = line_rectangle[::-1]
        line_rectangle = points_to_gdal_polygon(line_rectangle)
        line_polygon = line_rectangle.Intersection(area_gdal_polygon)
        if line_polygon.GetArea() < 0.0001:
            continue
        line_polygon_envelope = line_polygon.GetEnvelope()

        line_min_x, line_max_x = line_polygon_envelope[0], line_polygon_envelope    [1]
        line_length = line_max_x-line_min_x
        line_center_x = (line_min_x+line_max_x)/2.

        # 航线偏移(Sar)
        fly_y = None
        #if fly_right:
        fly_y = line_y + fly_position_left_offset_meters
        #else:
           # fly_y = line_y - fly_position_left_offset_meters

        line_fly_points = []
        point_idx = 0
        if shoot_mode == 'shutter':
            photos_num = math.ceil(line_length/forward_shooting_space_meters) +     1
            shoots_x = [forward_shooting_space_meters * (i-(photos_num-1)/2.) +     line_center_x for i in range(photos_num)]
            if not fly_right:
                shoots_x = shoots_x[::-1]

            for i in range(photos_num):
                infor = 'straight'
                if photos_num == 1 and i == 0:
                    infor = 'enter_and_leave'
                elif i == 0:
                    infor = 'enter'
                elif i == photos_num - 1:
                    infor = 'leave'

                shoot_x = shoots_x[i]

                geo_x, geo_y = one_point_coor_trans(shoot_x, fly_y,     inv_trans_mat)
                line_fly_points.append({
                    'number': point_idx,
                    'longitude': geo_x,
                    'latitude': geo_y,
                    'fly_height_m': fly_height_m,
                    'control_code': 'camera_shoot',
                    'infor': infor,
                })
                point_idx += 1
                photo_ground_rectangle = [
                    (shoot_x - photo_size_ground_meters_half_x, line_y -        photo_size_ground_meters_half_y),
                    (shoot_x - photo_size_ground_meters_half_x, line_y +        photo_size_ground_meters_half_y),
                    (shoot_x + photo_size_ground_meters_half_x, line_y +        photo_size_ground_meters_half_y),
                    (shoot_x + photo_size_ground_meters_half_x, line_y -        photo_size_ground_meters_half_y),
                ]
                photo_ground_rectangles.append(photo_ground_rectangle)
                photo_ground_rectangles_geo.append(coor_trans       (photo_ground_rectangle, inv_trans_mat))
        elif shoot_mode == 'sar' or shoot_mode == 'video':
            start_point, end_point = (line_min_x, fly_y), (line_max_x, fly_y)
            if not fly_right:
                start_point, end_point = end_point, start_point
            start_point_geo, end_point_geo = coor_trans([start_point, end_point]    , inv_trans_mat)
            line_fly_points.append({
                'number': point_idx,
                'longitude': start_point_geo[0],
                'latitude': start_point_geo[1],
                'fly_height_m': fly_height_m,
                'control_code': 'sar_on' if 'shoot_mode' == 'sar' else None,
                'infor': 'enter',
            })
            point_idx += 1
            line_fly_points.append({
                'number': point_idx,
                'longitude': end_point_geo[0],
                'latitude': end_point_geo[1],
                'fly_height_m': fly_height_m,
                'control_code': 'sar_off' if 'shoot_mode' == 'sar' else None,
                'infor': 'enter',
            })
            point_idx += 1

            photo_ground_rectangle = [
                (line_min_x, line_y - photo_size_ground_meters_half_y),
                (line_min_x, line_y + photo_size_ground_meters_half_y),
                (line_max_x, line_y + photo_size_ground_meters_half_y),
                (line_max_x, line_y - photo_size_ground_meters_half_y),
            ]
            photo_ground_rectangles.append(photo_ground_rectangle)
            photo_ground_rectangles_geo.append(coor_trans   (photo_ground_rectangle, inv_trans_mat))
        else:
            raise 'unknown shoot_mode : %s' % str(shoot_mode)

        lines.append({
            'points': line_fly_points,
            'length': get_meters_between_2_gps_points(
                line_fly_points[0]['longitude'],
                line_fly_points[0]['latitude'],
                line_fly_points[-1]['longitude'],
                line_fly_points[-1]['latitude'],),
        })
        fly_right = not fly_right

    debug_info = {
        'board_region': board_area_res,
        'shooting_area': shooting_area,
        'photo_ground_rectangles': photo_ground_rectangles,
        'area_gdal_polygon': area_gdal_polygon,
    }
    return lines, photo_ground_rectangles_geo, debug_info


def clock_to_float(hour, minute, sec):
    return hour + minute/60. + sec/3600.


def float_to_clock(float_hour):
    hour = math.floor(float_hour)
    left = (float_hour-hour)*60
    minute = math.floor(left)
    sec = (left-minute)*60
    return hour, minute, sec


def _get_pku_points_for_test():
    min_x_pku = clock_to_float(116, 17, 58.22)
    min_y_pku = clock_to_float(39, 59, 1.99)
    max_x_pku = clock_to_float(116, 18, 31.90)
    max_y_pku = clock_to_float(39, 59, 53.10)
    east_gate_x, east_gate_y = clock_to_float(116, 18, 32.67), clock_to_float(39, 59, 29.34)
    return min_x_pku, min_y_pku, max_x_pku, max_y_pku, east_gate_x, east_gate_y


def _get_pku_area_for_test():
    points_str = '116.2991669667795,39.99593801855181,0 116.2981599305666,39.99432479048227,0 116.2982396346779,39.99187193771684,0 116.2986316799483,39.98955010195986,0 116.2989869679613,39.98690346993811,0 116.2993415918365,39.98487013115884,0 116.3014506369334,39.98456502893167,0 116.3048729780067,39.98460101371672,0 116.3082952637886,39.98460289618692,0 116.3097550542167,39.98490898739406,0 116.3101420184187,39.98552190351396,0 116.3103273694663,39.98762327912843,0 116.3100035378802,39.98993170987488,0 116.3091165111576,39.99366244148697,0 116.3090918447541,39.99806538791157,0 116.3068805401394,39.99809843859089,0 116.3046713806594,39.9980566831553,0 116.3028156745741,39.99785113751588,0 116.3020342398605,39.99688750989205,0 116.301196064829,39.99633581837119,0 116.2991669667795,39.99593801855181,0'
    res = []
    for point_str in points_str.split(' '):
        x, y, _ = point_str.split(',')
        x, y = float(x), float(y)
        res.append((x, y))
    return res

def plan_a_route_for_test():
    import sys
    sys.path.append('..')
    import geo_polygons
    an_area = geo_polygons.Polygons.aoxiang['vertex']
    if not POLYGON_AS_CLOCKWISE:
        an_area = an_area[::-1]

    shoot_coors_geo, photo_ground_rectangles_geo, debug_info = route_planning(
        shooting_area=an_area,
        shooting_area_coor_egsp_code='4326',
        fly_direction=(1, 1),
        forward_shooting_space_meters=8,
        side_shooting_space_meters=16,
        forward_photo_ground_meters=10,
        side_photo_ground_meters=20,
        fly_height_m=1000,
        shoot_mode='shutter',
        fly_position_left_offset_meters=0,
        #aerocraft_num=1,
    )
    return shoot_coors_geo, photo_ground_rectangles_geo, debug_info


class _UnitTest(unittest.TestCase):
    def test_coor_trans(self):
        min_x_pku, min_y_pku, max_x_pku, max_y_pku, east_gate_x, east_gate_y = _get_pku_points_for_test()
        dis_meters = get_meters_between_2points(min_x_pku, min_y_pku, max_x_pku, max_y_pku, '4326')
        self.assertTrue(1700 < dis_meters and dis_meters < 1800)

        area_pku = [(min_x_pku, min_y_pku), (max_x_pku, max_y_pku), (max_x_pku, min_y_pku)]
        if not POLYGON_AS_CLOCKWISE:
            area_pku = area_pku[::-1]
        trans_mat, inv_trans_mat = get_coor_trans_mat(area_pku, '4326', (1, 1))
        trans_east_gate_x, trans_east_gate_y = one_point_coor_trans(east_gate_x, east_gate_y, trans_mat)
        self.assertTrue(trans_east_gate_x > 0 and trans_east_gate_y < 0)
        trans2_east_gate = one_point_coor_trans(trans_east_gate_x, trans_east_gate_y, inv_trans_mat)
        dis_trans2 = get_meters_between_2_gps_points(trans2_east_gate[0], trans2_east_gate[1], east_gate_x, east_gate_y)
        self.assertTrue(dis_trans2 < .1)

    def test_route_planning(self):
        shoot_coors_geo, photo_ground_rectangles_geo, debug_info = plan_a_route_for_test()

    def test_gdal_insection(self):
        poly1 = points_to_gdal_polygon([(1., 0.), (1., 3.), (2., 3.), (2., 0.)])
        poly2 = points_to_gdal_polygon([(0., 1.), (0., 2.), (3., 2.), (3., 1.)])
        intersection = poly1.Intersection(poly2)
        poly1 = points_to_gdal_polygon([(0., 0.), (0., 1.), (1., 1.), (1., 0.)])
        poly2 = points_to_gdal_polygon([(2., 2.), (2., 3.), (3., 3.), (3., 2.)])
        # poly2 = points_to_gdal_polygon([(1., 1.), (1., 3.), (3., 3.), (3., 1.)])
        intersection = poly1.Intersection(poly2)
        # print(intersection.GetArea())

    def test_get_meters_between_2points(self):
        self.assertTrue(get_meters_between_2points(0, 0, 1, 1, '4326') > 0)


if __name__ == '__main__':
    unittest.main()
