#中尺度
##处理过程
```
Step1. 获取基础信息(任务信息,飞机&传感器信息,地理信息,环境信息(天气等),任务开始和结束时间)  对应后端状态 Ready->Need_data
    create_mission(任务信息)
    add_data(任务信息)  
    add_data(飞机信息)  
    add_data(传感器信息)  
    add_data(地理信息)  
    add_data(环境信息) 
    add_data(任务开始和结束时间) 
    中间随时get_ui_display()  
Step2. 任务规划&航迹规划  对应后端状态 Need_data->Plan_Ready
    get_mission_planning_res()  
Step3. 结果在屏幕上显示  对应后端状态 Plan_Ready
    get_ui_display()  
Step4. 将规划结果发给控制中心  对应后端状态 Plan_Ready
    get_mission_planning_res()  
Step5. 后续实时更新快视图  对应后端状态 Run
    add_data(实时飞行数据)  
    get_ui_display()  
```

##四个观测场景——飞行状态
```
1.全区域观测【区域】
2.重灾区观测【区域】
3.死角区域观测【盘旋】
4.组合观测：全区域观测&重灾区观测&死角区域观测【区域，盘旋】（多种模式的组合）
```

##规划输入输出
###全区域观测/重灾区观测
```
input:
 任务信息：观测区域位置,要求的分辨率,要求的重叠率;
 飞机信息：类型,数量,速度,航高,航拍时间,航拍间隔;
 传感器信息:类型,数量,视场角,焦距;
 地理信息：全区域地理地图/重灾区地理地图;
 环境信息：天气,风力,降雨;
 任务开始和结束时间：*年*月*日*时*分*秒-*年*月*日*时*分*秒;

Process:  
 航迹规划 - 计算航迹(考虑航高等);

output:
 屏幕输出:  
 航迹预设显示,飞机显示模拟;
 模拟快视图显示;
 向控制中心输出:  
 任务类型 - 区域拍摄;
 航迹规划 - 飞行高度,飞行速度,航迹;
```

###死角区域观测
```
input:
 任务信息：观测区域位置,要求的分辨率,盘旋中心,盘旋直径;
 飞机信息：类型,数量,速度,航高,航拍时间,航拍间隔;
 传感器信息:类型,数量,视场角,焦距;
 地理信息：死角区域地理地图;
 环境信息：天气,风力,降雨;
 任务开始和结束时间：*年*月*日*时*分*秒-*年*月*日*时*分*秒;

Process:  
 航迹规划 - 计算航迹(考虑航高等);

output:
 屏幕输出:  
 航迹预设显示,飞机显示模拟;
 模拟快视图显示;
 向控制中心输出:  
 任务类型 - 区域拍摄;
 航迹规划 - 飞行高度,飞行速度,盘旋中心,盘旋路径; 
```

###组合观测
```
三种观测方式的组合,输入和输出分别如上;
```
