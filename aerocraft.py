# coding=utf8
'''
class Aerocraft():
    def __init__(self,
                 type_=None,
                 max_speed_meter_per_second=None, min_speed_meter_per_second=None, normal_speed_meter_per_second=None,
                 max_height_meter=None, min_height_meter=None, normal_height_meter=None,
                 max_distance_meter=None, residual_energy_percent=1,
                 ):
        self.type = type_  # 飞行器类型
        self.max_speed_meter_per_second=max_speed_meter_per_second  # 最大航速/(m/s)
        self.min_speed_meter_per_second=min_speed_meter_per_second  # 最小航速/(m/s)
        self.normal_speed_meter_per_second=normal_speed_meter_per_second  # 正常航速/(m/s)
        self.max_height_meter=max_height_meter  # 最大航高/m
        self.min_height_meter=min_height_meter  # 最小航高/m
        self.normal_speed_meter_per_second=normal_height_meter  # 正常航高/m
        self.max_distance_meter=max_distance_meter  # 最大航程/m
        self.residual_energy_percent=residual_energy_percent  # 剩余能量百分比
'''
aerocrafts = {
    '轻小型固定翼无人机': {
        'name': '轻小型固定翼无人机',
        'max_v_km_h': 120,
        'suggest_v_km_h': 120,
        'min_v_km_h': 80,
        'max_height_m': 2000,
        'min_height_m': 100,
    },
    '长航时固定翼无人机': {
        'name': '长航时固定翼无人机',
        'max_v_km_h': 180,
        'suggest_v_km_h': 180,
        'min_v_km_h': 150,
        'max_height_m': 5000,
        'min_height_m': 100,

    },
    '多旋翼无人机': {
        'name': '多旋翼无人机',
        'max_v_km_h': 20,
        'suggest_v_km_h': 20,
        'min_v_km_h': 0,
        'max_height_m': 800,
        'min_height_m': 10,
    }
}