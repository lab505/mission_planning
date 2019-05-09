# coding=utf8

cameras = {
    'minisar': {
        'type': 'sar',
        'name': 'minisar',
        'R_min_m': 3000.,
        'R_max_m': 4000.,
        'R_suggest_m': 3500.,
        'ground_resolution_m': .1,
        'right_look_angle_degrees': 45.,
        'range_beam_width_degrees': 6.,
    },
    '大视场立体测绘相机': {
        'type': 'camera',
        'name': '大视场立体测绘相机',
        'f_m': 3.3*0.001,
        'pixel_size_m': 0.1*0.001*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,
    },
    '可见光视频相机': {
        'type': 'camera',
        'name': '可见光视频相机',
        'f_m': 6.6*0.001,
        'pixel_size_m': 0.1*0.001*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,

    },
    '红外视频相机': {
        'type': 'camera',
        'name': '红外视频相机',
        'f_m': 6.6*0.001,
        'pixel_size_m': 0.1*0.001*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,

    },
    'Canon EOS 450D': {
        'type': 'camera',
        'name': 'Canon EOS 450D',
        'f_m': 24*0.001,
        'pixel_size_m': 5.2*0.001*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,
    },
    '大视场立体测绘相机': {
        'type': 'camera',
        'name': '大视场立体测绘相机',
        'f_m': 44*0.001,
        'pixel_size_m': 1.01*0.001*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,
    },
    '双波段视频吊舱': {
        'type': 'camera',
        'name': '双波段视频吊舱',
        'f_m': 24*0.001,
        'pixel_size_m': 25*0.001*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,
    },
    '高光谱相机': {
        'type': 'camera',
        'name': '高光谱相机',
        'f_m': 8*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,
    },
    '偏振相机': {
        'type': 'camera',
        'name': '偏振相机',
        'f_m': 50*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,
    },
    '多光谱相机': {
        'type': 'camera',
        'name': '多光谱相机',
        'f_m': 35*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,
    },
     '全色相机': {
        'type': 'camera',
        'name': '全色相机',
        'f_m': 30*0.001,
        'pixel_num_x': 1920,
        'pixel_num_y': 1080,
    }
    
}
