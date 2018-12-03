# coding:utf-8
import argparse, sys
import mission_planning

parser = argparse.ArgumentParser()

parser.add_argument("-mysql_conf_file", default="/Users/cjl/.my.cnf")
subparsers = parser.add_subparsers(dest='command')

subp_ = subparsers.add_parser("create_mission")
subp_.add_argument('-input')
subp_ = subparsers.add_parser("add_data")
subp_.add_argument('-input')
subp_ = subparsers.add_parser("get_main_ui_display")
subp_ = subparsers.add_parser("get_mission_planning_res")
subp_ = subparsers.add_parser("get_status")
kwargs = vars(parser.parse_args())

res = None
if kwargs['command'] == 'create_mission':
    res = mission_planning.create_mission(kwargs['input'], mysql_conf_file=kwargs['mysql_conf_file'])
elif kwargs['command'] == 'add_data':
    res = mission_planning.add_data(kwargs['input'], mysql_conf_file=kwargs['mysql_conf_file'])
elif kwargs['command'] == 'get_main_ui_display':
    res = mission_planning.get_main_ui_display(mysql_conf_file=kwargs['mysql_conf_file'])
elif kwargs['command'] == 'get_mission_planning_res':
    res = mission_planning.get_mission_planning_res(mysql_conf_file=kwargs['mysql_conf_file'])
elif kwargs['command'] == 'get_status':
    res = mission_planning.get_status(mysql_conf_file=kwargs['mysql_conf_file'])
else:
    res = 'unknown command'

print (str(res))