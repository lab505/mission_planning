# coding=utf8

cameras = {
    'minisar': {
        'type': 'sar',#载荷类型
        'name': 'minisar',#载荷名字
        'R_min_m': 800.,#最短波长
        'R_max_m': 6000.,#最长波长
        'R_suggest_m': 800.,#建议波长
        'f_m': -1.,#焦距
        'ground_resolution_m': .1,#地面分辨率
        'right_look_angle_degrees': -66.,#安装角度
        'range_beam_width_degrees': 13.,#波束宽度
    },

    '广域SAR': {
        'type': 'sar',
        'name': '广域SAR',
        'R_min_m': 30000.,
        'R_max_m': 40000.,
        'R_suggest_m': 30000.,
        'ground_resolution_m': .2,
        'right_look_angle_degrees': 80.,
        'range_beam_width_degrees': 5.,
    },

    '大视场立体测绘相机': {
        'type': 'camera',
        'name': '大视场立体测绘相机',
        'f_m': 35*0.001,
        'pixel_size_m': 3.76*0.001*0.001,
        'pixel_num_x': 11664,
        'pixel_num_y': 8750,
    },

    '地理所单电数码相机': {
        'type': 'camera',
        'name': '地理所单电数码相机',
        'f_m': 35*0.001,
        'pixel_size_m': 6*0.001*0.001,
        'pixel_num_x': 7952,
        'pixel_num_y': 5304,
    },

    '高光谱相机': {
        'type': 'camera',
        'name': '高光谱相机',
        'f_m': 13.2*0.001,
        'pixel_size_m': 6.5*0.001*0.001,
        'pixel_num_x': 2000,
        'pixel_num_y': 2054,
    },

    '轻型双波段相机(可见光)': {
        'type': 'video',
        'name': '轻型双波段相机(可见光)',
        'f_min_m':4.7*0.001,
        'f_max_m':47*0.001,
        'f_m': 20*0.001,
        'pixel_size_m': 2.8*0.001*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,  
    },

    '轻型双波段相机(红外)': {
        'type': 'video',
        'name': '轻型双波段相机(红外)',
        'f_m': 35*0.001,
        'pixel_size_m': 17*0.001*0.001,
        'pixel_num_x': 1024,
        'pixel_num_y': 768,  
    },
    
     '多光谱相机': {
        'type': 'camera',
        'name': '多光谱相机',
        'f_m': 6*0.001,
        'pixel_size_m': 3.75*0.001*0.001,
        'pixel_num_x': 1280,
        'pixel_num_y': 960,
    },

     '光学相机（视频）': {
        'type': 'video',
        'name': '光学相机（视频）',
        'f_m': 8*0.001,
        'pixel_size_m': 3*0.001*0.001,
        'pixel_num_x': 320,
        'pixel_num_y': 240,
    },
    
    '光学相机（照片）': {
        'type': 'camera',
        'name': '光学相机（照片）',
        'f_m': 35*0.001,
        'pixel_size_m': 2.41*0.001*0.001,
        'pixel_num_x': 5472,
        'pixel_num_y': 3648,
    },

}
