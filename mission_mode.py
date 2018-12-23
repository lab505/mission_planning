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
                            sensor='visible light',
                            sensor_num=1),
                    ],
                ),
            ],
        )
        print (mission_plan(request))
    test_small_scale()