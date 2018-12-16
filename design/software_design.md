# 后端状态
![](figures/backend_status.png)

### Ready
#### 前端显示
已有的地理数据
### Need data
#### 前端显示
已有的信息
### Plan ready
#### 前端显示
任务信息,规划模拟
### Run
#### 前端显示
飞行模拟,快视图等

# 任务模式
### 区域拍摄  
```
Input:  
任务信息 - 区域具体位置,要求分辨率,要求重叠度  
飞机信息 - 航速,航程,飞行高度  
传感器信息 - 分辨率,视场大小,焦距  
  
Process:  
航迹规划 - 计算航迹(考虑重叠度,视场大小等)  
  
Output:  
屏幕输出:  
 航迹预设显示,飞机显示模拟  
向控制中心输出:  
 任务类型 - 区域拍摄
 航迹规划 - 飞行高度,飞行速度,航迹  
```
  
### 盘旋拍摄  
```
Input:  
任务信息 - 区域具体位置,盘旋直径,要求分辨率,要求周期  
飞机信息 - 航速,航程,飞行高度  
传感器信息 - 分辨率,视场大小,焦距  
  
Process:  
航迹规划 - 计算航迹(考虑航高等)  
  
Output:  
屏幕输出:  
 航迹预设显示,飞机显示模拟  
向控制中心输出:  
 任务类型 - 盘旋拍摄
 航迹规划 - 飞行高度,飞行速度,盘旋中心,盘旋直径(路径)  
```
### 跟踪拍摄  
```
Input:
任务信息 - 目标描述(初始位置)
Output:  
任务类型 - 跟踪
任务规划 - 目标描述(初始位置)
```

### 定点拍摄  
```
Input:
任务信息 - 目标位置
Output:  
任务类型 - 定点拍摄
任务规划 - 目标位置
```