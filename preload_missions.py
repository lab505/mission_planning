# coding=utf8

missions = {
    '中尺度_区域1_0.3m_可见光': {
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '可见光视频相机',
        'ground_resolution_m': 0.3,
        'fly_east_west_direction': True,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.3m_红外': {
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '红外视频相机',
        'ground_resolution_m': 0.3,
        'fly_east_west_direction': True,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域2_4m_EOS450D': {
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': 'Canon EOS 450D',
        'ground_resolution_m': 4,
        'fly_east_west_direction': True,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '小尺度_区域1_0.1m': {
        'application': '反恐',
        'aerocraft': '多旋翼无人机',
        'cameras': 'Canon EOS 450D',
        'ground_resolution_m': 0.1,
        'fly_east_west_direction': True,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '小尺度_区域1_1m': {
        'application': '反恐',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '双波段视频吊舱',
        'ground_resolution_m': 1,
        'fly_east_west_direction': True,
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
}