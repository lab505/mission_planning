# 任务规划软件状态
## 状态转移图
![](figures/backend_status.png)

## 各种状态
### Ready
```
状态描述: 没有创建任务的最初状态
前端显示: 已有的地理数据/天气数据
可以执行的操作: create_mission(任务基础信息), add_data(地理/地图/台站/天气)
状态跃迁: create_mission()进入need_data状态
```
### Need data
```
状态描述: 已经创建任务,但信息不足作出任务规划
前端显示: 已有的地理数据/天气数据, 已有的飞机/传感器数据, (可选: 显示缺失哪些数据)
可以执行的操作: add_data(地理/地图/台站/天气), add_data(飞机/传感器)
状态跃迁: 有足够的数据进行规划进入plan_ready状态, initialize()进入ready状态
```
### Plan ready
```
状态描述: 任务规划完成,还没开始飞
前端显示: 已有的地理数据/天气数据, 已有的飞机/传感器数据, 任务模拟显示
可以执行的操作: run()
状态跃迁: run() 进入plan running状态, initialize()进入ready状态
```
### Plan running
```
状态描述: 正在飞
前端显示: 各种数据, 快视图, 飞行模拟
可以执行的操作: add_data(real_time_pos), add_data(quick_view_image)
状态跃迁: initialize()进入ready状态
```
### 所有状态均可执行的操作
```
initialize() 删除所有信息,初始化
get_ui_display() 获取前端显示
add_data(地理/地图/台站/天气)
```
