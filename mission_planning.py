import json

def create_mission(input_):
    return json.dumps({'res': True})

def add_data(input_):
    return json.dumps({'res': True})

def get_main_ui_display(input_=None):
    res = {
        'title': 'main_window_1',
        'mission_type': 'large_scale'
    }
    return json.dumps(res)

def get_mission_planning_res(input_=None):
    res = {
        'name': 'mission1',
        'mission_type': 'large_scale',
        'mission_area': [(116.6523885,36.9449586),(116.6523645,36.9443586),(116.6677850,36.9536846),(116.6677474,36.9536833),(116.6677848,36.9536836)]
    }
    return json.dumps(res)
