# coding=utf8

cameras = {
    'minisar': {
        'type': 'sar',
        'name': 'minisar',
        'R_min_m': 1000.,
        'R_max_m': 6000.,
        'R_suggest_m': 1000.,
        'ground_resolution_m': .1,
        'right_look_angle_degrees': 70.,
        'range_beam_width_degrees': 6.,
    },

    #'广域SAR': {
       # 'type': 'sar',
        #'name': '广域SAR',
       # 'R_min_m': 3000.,
       # 'R_max_m': 4000.,
        #'R_suggest_m': 4000.,
        #'ground_resolution_m': .1,
        #'right_look_angle_degrees': 45.,
       # 'range_beam_width_degrees': 6.,
    #},

    '大视场立体测绘相机': {
        'type': 'camera',
        'name': '大视场立体测绘相机',
        'f_m': 35*0.001,
        'pixel_size_m': 3.76*0.001*0.001,
        'pixel_num_x': 11664,
        'pixel_num_y': 8750,
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
        'f_m': 8.4*0.001,
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
