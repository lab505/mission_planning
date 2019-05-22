output = {
    "mission_num": 15, //任务序号1-32
    "mission_name": "区域巡航15", //任务名称
    "board_region": [ //可飞行区域, 一个简单多边形, 目前由任务区域求5000m缓冲区得到
        {
		    "number": 1,
            "longitude": 133.564,
            "latitude": 34.2654,
		},
        {
		    "number": 2,
            "longitude": 114.235,
            "latitude": 34.568,
		},
        {
		    "number": 3,
            "longitude": 113.456,
            "latitude": 36.456,
		},
    ],
    "route_coors": [ //拍摄点
        {
			"number": 1, 
			"longitude": 133.564, 
			"latitude": 34.2654,
			"fly_height_m": 888,
			"control_code": "camera_shoot",
			"infor": "enter",
		},
		{
			"number": 2, 
			"longitude": 133.664, 
			"latitude": 34.2554,
			"fly_height_m": 888,
			"control_code": "camera_shoot",
			"infor": "straight",
        },
		{
			"number": 3, 
			"longitude": 133.764, 
			"latitude": 34.2454,
			"fly_height_m": 888,
			"control_code": "camera_shoot",
			"infor": "leave",
        },
    ],
    "plane": { // 飞机信息
        "platform_type": 1, // 平台类型
        "plane_num": 3, //飞机编号
        "fly_time_hours": 'unknown', //最大航时
        "mincycle": 'unknown', // 最小转弯半径
        "maxclimbrate": 'unknown',//飞机最大爬升率
    },
    "camera": { // 载荷信息
        "camera_type": "visible_light_camera",
    },
    "wind_direction": 60,  // 东偏北60度
}
