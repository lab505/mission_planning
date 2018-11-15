import json, logging
import main

'''
第三课题任务规划软件的交互模块demo
'''
Dict1= [data1, data2,...]
#每个data为一个dict
#e.g.:data1={type: 资源类型（对应resources_data的具体资源,
#resources_data: 具体资源(快视图,全国站点图,全国站点坐标信息，参与观测无人机实时GPS坐标数据)}
#data2={type:资源类型,resources_data: 具体资源}
MP1=new Mission_Planning
MP1.add_data=(Dict1)#数据加载


##任务创建
'''
    由应用方/操作人员调用
    输入
    name: 任务名,字符串类型
    mission_type: in ['large_scale', 'midium_scale', 'small_scale']
    mission_level: in ['science_experiment', 'normal_mission', 'urgent_mission']
    mission_area: 任务地理区域, [(x1,y1),(x2,y2)...] 一个由list表示的多边形
    weather_condition: in ['rainy', 'sunny', ......]
    wind: in [0,1,2,3,4...]#数字代表风力级别
    sensor: in ['optical', 'nir', ...]
    platform: in ['multi-rotors', 'fixed-wing', ...]
    flying_height: [min_height, max_height]
    flying_speed: [min_speed, max_speed]
    shooting_space_seconds: [min_space, max_space]#拍摄间隔
    begin_time: like '2018-11-13-14-00'
    end_time: like '2018-11-13-14-00'
    返回
    任务创建的结果:成功or失败
    '''
MP1.create_mission(‘禹城区大尺度植被长势监测任务',large_scale,science_experiment, 
[(116.6523885,36.9449586),(116.6523645,36.9443586),(116.6677850,36.9536846),(116.6677474,36.9536833),(116.6677848,36.9536836)]，
'sunny',1,'optical'，'fixed-wing'，·[75,75]，[69,69]#固定翼无人机飞行高度为15-91m;飞行速度是69公里每小时
[0.05,0.06],'2019-11-13-14-00'，'2019-11-13-14-00')
#坐标基于全国野外台站点经纬度坐标数据，x*和y*都是经纬度坐标
Dict2= [data3, data4,...]
MP1.add_data=(Dict2)#数据补充
#返回的dict有'title'(主程序标题)和'mission_type'(界面上的任务类型)
ui_display = MP1.get_main_ui_display() #获取主界面显示内容

## 获取规划结果
mission_ = MP1.get_mission_planning_res()

#添加实时飞行数据,刷新显示结果
Dict3=[data5, data6,...]
MP1.add_data(Dict3)#实时飞行数据
ui_display = MP1.get_main_ui_display() 获取主界面显示内容
