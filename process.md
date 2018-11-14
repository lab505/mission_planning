# 外部调用过程初步设计

## 1.创建任务阶段
```
mp = new Mission_Planning
mp.add_data(添加一些初始化地理数据)
mp.create_mission(提供任务基础信息)
mp.add_data(可以提供一些补充信息)
ui_display = mp.get_main_ui_display() 获取主界面显示内容
```

## 2.获取规划结果
```
mission_ = mp.get_mission_planning_res()
```

## 3.添加实时飞行数据,刷新显示结果结果
```
mp.add_data(实时数据)
ui_display = mp.get_main_ui_display() 获取主界面显示内容
```
