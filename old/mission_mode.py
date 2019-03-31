# coding=utf8
from aerocraft import Aerocraft
import flight_mode

class SingleMission():
    def __init__(self,
                 name=None,
                 flight_tasks=[]):
        self.name = name
        self.flight_tasks = flight_tasks

class MissionModePlanRequest():
    def __init__(self,
                 missionmode=None,
                 missions=[]):
        self.missionmode=missionmode
        self.missions=missions


def mission_plan(missionrequest):
    response = {}
    assert missionrequest.missionmode in [
        'Single_Mission_Single_Point',  # 单点单任务
        'Single_Mission_Multi_Point',  # 多点单任务
        'Multi_Mission_Single_Point',  # 单点多任务
        'Multi_Mission_Multi_Point',  # 多点多任务
        ]
    
    # 任务规划
    response['plan'] = {}
    for single_mission in missionrequest.missions:  # 每个任务
        single_mission_plan = []
        for flight_task in single_mission.flight_tasks:  # 这个点里的每个任务
            single_mission_plan.append(flight_mode.flight_plan(flight_task))
        response['plan'][single_mission.name] = single_mission_plan
    return response

if __name__ == '__main__':
    def test_small_scale():
        request = MissionModePlanRequest(
            missionmode='Single_Mission_Single_Point',
            missions=[
                SingleMission(
                    name='抓捕过程监测',
                    flight_tasks=[
                        flight_mode.FightPlanRequest(
                            flightmode='Fixed_Gaze',
                            target=(120.1234,40.1234),
                            aerocraft=Aerocraft(
                                type_='quadrotor'),
                            aerocraft_num=1,
                            sensors_per_aerocraft=['visible light'],
                            surface_resolution=1,
                            begin_time='2018-12-32 08:00:00'
                            ),
                    ],
                ),
            ],
        )
        print (mission_plan(request))
    test_small_scale()

    def test_large_scale():
        request = MissionModePlanRequest(
            missionmode='Multi_Mission_Single_Point',
            missions=[
                SingleMission(
                    name='单点多任务区域监测',
                    flight_tasks=[
                        flight_mode.FightPlanRequest(
                            flightmode='Polygon',
                            target=[(128.1234,39.1234),(119.1234,39.1234),(120.2234,39.2234),(120.1254,40.1264)],
                            aerocraft=Aerocraft(
                                type_='quadrotor'),
                            aerocraft_num=1,
                            sensors_per_aerocraft=['visible light'],
                            surface_resolution=0.2,
                            begin_time='2019-3-3 08:20:00'
                            ),
                    ],
                ),
            ],
        )
        print (mission_plan(request))
    test_large_scale()