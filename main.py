import json

class Mission_Planning(object):
    def __init__(self):
        pass
    
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