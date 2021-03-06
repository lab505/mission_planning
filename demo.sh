python3 main.py create_mission -input "{\"shooting_space_seconds\": [0.05, 0.06], \"mission_type\": \"large_scale\", \"mission_level\": \"science_experiment\", \"begin_time\": \"2019-11-13-14-00\", \"name\": \"\\u79b9\\u57ce\\u533a\\u5927\\u5c3a\\u5ea6\\u690d\\u88ab\\u957f\\u52bf\\u76d1\\u6d4b\\u4efb\\u52a1\", \"mission_area\": [[116.6523885, 36.9449586], [116.6523645, 36.9443586], [116.667785, 36.9536846], [116.6677474, 36.9536833], [116.6677848, 36.9536836]], \"sensor\": \"optical\", \"flying_speed\": [69, 69], \"platform\": \"fixed-wing\", \"end_time\": \"2019-11-13-14-00\", \"flying_height\": [75, 75], \"wind\": 1, \"weather_condition\": \"sunny\"}"
python3 main.py add_data -input  "[{\"data\": \"1234567\", \"type\": \"geo_data\"}, {\"data\": \"1234567\", \"type\": \"platform_data\"}]"
python3 main.py get_main_ui_display
python3 main.py get_mission_planning_res

python3 main.py add_data -input  "{\"data_type\": \"uav\", \"data\": [{\"id\": \"12345\", \"type\": \"gudingyi\"}, {\"id\":\"543\" , \"type\": \"type2\"}]}"
python3 main.py add_data -input  "{\"data_type\": \"sensor\", \"data\": [{\"id\": \"12345\", \"type\": \"kejianguang\"}, {\"id\":\"543\" , \"type\": \"rehongwai\"}]}"
python3 main.py add_data -input  "{\"data_type\": \"station\", \"data\": [{\"id\": 12, \"zuobiao\": \"[118.245,38.456]\"}, {\"id\": 23, \"zuobiao\": \"[117.245,39.453]\"}]}"
python3 main.py add_data -input  "{\"data_type\": \"weather\", \"data\": \"sunny\"}"



'''
import json
uav1={'id':12345,'type':'gudingyi'}
uav2={'id':543,'type':'type2'}
uav_data=[uav1,uav2]
json.dumps(uav_data)
'''
