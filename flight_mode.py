# coding=utf8
from aerocraft import Aerocraft

class FightPlanRequest():
    def __init__(self,
                 flightmode=None,
                 target=None, 
                 aerocraft=None,
                 aerocraft_num=1, 
                 sensor=None,
                 sensor_num=1):
        self.flightmode = flightmode
        self.target = target
        self.aerocraft = aerocraft
        self.aerocraft_num = aerocraft_num
        self.sensor = sensor
        self.sensor_num = sensor_num


def flight_plan(flightrequest):
    response = {}
    assert type(flightrequest) is FightPlanRequest
    assert type(flightrequest.aerocraft) is Aerocraft
    if flightrequest.flightmode is 'Polygon':  # 区域飞行
        response['flightmode'] = 'Polygon'
        # TODO做任务规划
        pass
    elif flightrequest.flightmode is 'Circle':  # 盘旋
        response['flightmode'] = 'Circle'
        # TODO做任务规划
        pass 
    elif flightrequest.flightmode is 'Tracking':  # 跟踪
        response['flightmode'] = 'Tracking'
        # TODO做任务规划
        pass 
    elif flightrequest.flightmode is 'Fixed_Gaze':  # 定点凝视
        response['flightmode'] = 'Fixed_Gaze'
        # TODO做任务规划
        pass
    else:
        raise 'unknown flight mode %s' % str(flightrequest.flightmode)
    return response