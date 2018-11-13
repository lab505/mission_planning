import json

class Mission_Planning(object):
    def __init__(self):
        pass
    
    '''
    输入
    mission_type: in ['large_scale', 'midium_scale', 'small_scale']
    mission_level: in ['science_experiment', 'normal_mission', 'urgent_mission']
    weather_condition: in ['rainy', 'sunny', ......]
    wind: in [1,2,3,4]
    sensor: in ['optical', 'nir', ...]
    begin_time: like '2018-11-13-14-00'
    end_time
    '''
    def create_mission(self, input_):
        assert isinstance(input_, str)
        input_ = json.loads(input_)
        assert 'name' in input_


        res = {}
        res['create_res'] = True
        res['reply'] = 'create_success'
        return json.dumps(res)
    
    def add_data(self, input_):
        pass
    
    def get_display(self):
        pass
    
    def get_mission_planning_res(self, input_):
        pass
        #