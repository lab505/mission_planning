# coding:utf-8
import json, logging
from main import Mission_Planning

'''
第三课题任务规划软件的交互模块demo
'''

# 初始化资源
MP1= Mission_Planning()

# DEMO_1 : 任务创建
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
input_dict_={'name':'禹城区大尺度植被长势监测任务','mission_type':'large_scale','mission_level':'science_experiment','mission_area':
             [(116.6523885,36.9449586),(116.6523645,36.9443586),(116.6677850,36.9536846),(116.6677474,36.9536833),(116.6677848,36.9536836)],
             'weather_condition':'sunny','wind':1,'sensor':'optical','platform':'fixed-wing','flying_height':[75,75],'flying_speed':[69,69],
             'shooting_space_seconds':[0.05,0.06],'begin_time':'2019-11-13-14-00','end_time':'2019-11-13-14-00'}
             #固定翼无人机飞行高度为15-91m;飞行速度是69公里每小时
             #坐标基于全国野外台站点经纬度坐标数据，x*和y*都是经纬度坐标 
output_dict_={} 
output_dict_=MP1.create_mission(json.dumps(input_dict_))
#print(output_dict_)  #输出结果


# DEMO_2 : 添加数据
# 每个data为一个dict
# e.g.:some_data={type: 资源类型（对应resources_data的具体资源,
# resources_data: 具体资源(快视图,全国站点图,全国站点坐标信息，参与观测无人机实时GPS坐标数据)}
# data2={type:资源类型,resources_data: 具体资源}
# MP1= New Mission_Planning
data1 = {'type': 'geo_data', 'data': '1234567'}
data2 = {'type': 'platform_data', 'data': '1234567'}
some_data= [data1, data2]
MP1.add_data=(json.dumps(some_data))#数据补充

# DEMO_3 : 获取界面显示
#返回的dict有'title'(主程序标题)和'mission_type'(界面上的任务类型)等显示信息
ui_display = MP1.get_main_ui_display() # 获取主界面显示内容, 刷新前端显示
print 'DEMO_3 界面显示:\n%s\n' % ui_display

# DEMO_4 : 获取规划结果
mission_ = MP1.get_mission_planning_res()
print 'DEMO_4 任务规划:\n%s\n' % mission_

# DEMO_5 : 添加实时飞行数据,刷新显示结果
data_camera_pos = {'type': 'camera_pos_data', 'data': '1234567'}
data_list = [data_camera_pos]
MP1.add_data=(json.dumps(data_list))
ui_display = MP1.get_main_ui_display() # 获取主界面显示内容,刷新前端显示
print 'DEMO_5 刷新后的显示:\n%s\n' % ui_display