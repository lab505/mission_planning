# coding:utf-8
import mission_planning, json, sys

testdata = {
    'area_points_list': [(30, 30), (30, 30.01), (30.01, 30.01), (30.01, 30)],
    'mission_name': 'mission1',
    'aerocraft': '猛牛-轻小型固定翼无人机(演示短航程)',
    'camera': '大视场立体测绘相机',
    'ground_resolution_m': 0.05,
    'forward_overlap': 0.4,
    'sideway_overlap': 0.6,
    'fly_direction_degree': 0,
    'application': 'flood',
    'board_region': None,
    'board_region_max_fly_height_m': 1000,
    'right_look_angle_degrees': 75,
    'R_suggest_m': 3000,
    'f_m': 0.035,
    'bend_radius': 200,

}


def plan(input_):
    succ, res = mission_planning.mission_planning(
        area_points_list=input_['area_points_list'],
        mission_name=input_['mission_name'],
        aerocraft=input_['aerocraft'],
        camera=input_['camera'],
        ground_resolution_m=input_['ground_resolution_m'],
        forward_overlap=input_['forward_overlap'],
        sideway_overlap=input_['sideway_overlap'],
        fly_direction_degree=input_['fly_direction_degree'],
        aerocraft_num=0,
        application=input_['application'],
        board_region=input_['board_region'],
        board_region_max_fly_height_m=input_['board_region_max_fly_height_m'],
        right_look_angle_degrees=input_['right_look_angle_degrees'],
        R_suggest_m=input_['R_suggest_m'],
        f_m=input_['f_m'],
        bend_radius=input_['bend_radius']
    )
    if succ:
        print(json.dumps(res).replace(' ', ''))
    else:
        print('failed')
        print(res)

def print_test_data():
    a = (json.dumps(testdata).replace(' ', ''))
    a = ('\\\"').join(a.split('\"'))
    print(a)

def test():
    plan(testdata)

def main(input_):
    input_ = json.loads(input_)
    plan(input_)

if __name__ == '__main__':
    input_ = sys.argv[1]

    if input_ == 'test':
        test()
    elif input_ == 'print_test_data':
        print_test_data()
    else:
        main(input_)