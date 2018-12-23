# coding=utf8
from aerocraft import Aerocraft

class FightPlanRequest():
    def __init__(self,
                 flightmode=None,
                 target=None,  # 目标,可以是多边形,或者点
                 aerocraft=None,  # 飞机类型&参数, Aerocraft类的实例
                 aerocraft_num=1,
                 sensors_per_aerocraft=[],  # 每台飞机搭载的传感器 TODO:参考Aerocraft类实现Sensor类
                 surface_resolution=None,  # 地表分辨率
                 begin_time=None,  # 任务开始时间
                 ):
        self.flightmode = flightmode
        self.target = target
        self.aerocraft = aerocraft
        self.aerocraft_num = aerocraft_num
        self.sensors_per_aerocraft = sensors_per_aerocraft
        self.surface_resolution=surface_resolution
        self.begin_time=begin_time


def flight_plan(flightrequest):
    response = {}
    assert isinstance(flightrequest, FightPlanRequest)
    assert isinstance(flightrequest.aerocraft, Aerocraft)
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