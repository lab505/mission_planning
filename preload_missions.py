# coding=utf8

missions = {
    '大尺度_区域1_10m_高光谱':{
       'application': '生态',
        'aerocraft': '轻小型无人机(1)',
        'cameras': '高光谱相机(1)',
        'ground_resolution_m':0.5,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_1m_视频吊舱':{
       'application': '生态',
        'aerocraft': '轻小型无人机(1)',
        'cameras': '视频吊舱(1)',
        'ground_resolution_m':1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
     '大尺度_区域1_1m_可见光':{
       'application': '生态',
        'aerocraft': '轻小型无人机(78)',
        'cameras': '可见光相机(78)',
        'ground_resolution_m':1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
      '大尺度_区域1_1m_MiniSAR':{
       'application': '生态',
        'aerocraft': '轻小型无人机(1)',
        'cameras': 'MiniSAR(1)',
        'ground_resolution_m':0.1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
     '大尺度_区域1_10m_高光谱':{
       'application': '生态',
        'aerocraft': '轻小型固定翼无人机(1)',
        'cameras': '高光谱相机(1)',
        'ground_resolution_m':0.5,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
     '大尺度_区域1_3.5m_偏振相机':{
       'application': '生态',
        'aerocraft': '轻小型固定翼无人机(3)',
        'cameras': '偏振光学相机(3)',
        'ground_resolution_m':3.5,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_2.5m_多光谱相机':{
       'application': '生态',
        'aerocraft': '轻小型固定翼(2)',
        'cameras': 'MiniSAR(1)+视频吊舱(1)',
        'ground_resolution_m':0.1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_1m_可见光':{
       'application': '生态',
        'aerocraft': '轻小型多旋翼无人机(19)',
        'cameras': '可见光相机(19)',
        'ground_resolution_m':1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_0.8m_全色':{
       'application': '生态',
        'aerocraft': '轻小型多旋翼无人机(4)',
        'cameras': '全色相机(4)',
        'ground_resolution_m':0.8,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '大尺度_区域1_0.8m_全色':{
       'application': '生态',
        'aerocraft': '轻小型多旋翼无人机(3)',
        'cameras': '多光谱相机(3)',
        'ground_resolution_m':0.8,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3, 
    },
    '中尺度_区域1_0.1m_广域SAR': {
        'application': '洪涝',
        'aerocraft': '长航时固定翼无人机',
        'cameras': '广域SAR',
        'ground_resolution_m': 0.1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.1m_minisar': {
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': 'minisar',
        'ground_resolution_m': 0.1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.1m_大视场立体测绘相机': {
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '大视场立体测绘相机',
        'ground_resolution_m': 0.1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '中尺度_区域1_0.1m_可见光': {
        'application': '洪涝',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '轻型双波段相机',
        'ground_resolution_m': 0.1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    
    '小尺度_区域1_0.1m': {
        'application': '反恐',
        'aerocraft': '多旋翼无人机',
        'cameras': 'Canon EOS 450D',
        'ground_resolution_m': 0.1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
    '小尺度_区域1_1m': {
        'application': '反恐',
        'aerocraft': '轻小型固定翼无人机',
        'cameras': '双波段视频吊舱',
        'ground_resolution_m': 1,
        'fly_direction': (1, 0),
        'forward_overlap': 0.6,
        'sideway_overlap': 0.3,
    },
}
