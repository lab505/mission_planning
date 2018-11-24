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

opts = {
    'create_mission': lambda: mission_planning.create_mission(kwargs['input'], mysql_conf_file=kwargs['mysql_conf_file']),
    'add_data': lambda: mission_planning.add_data(kwargs['input'], mysql_conf_file=kwargs['mysql_conf_file']),
    'get_main_ui_display': lambda: mission_planning.get_main_ui_display(mysql_conf_file=kwargs['mysql_conf_file']),
    'get_mission_planning_res': lambda: mission_planning.get_mission_planning_res(mysql_conf_file=kwargs['mysql_conf_file']),
    'get_status': lambda: mission_planning.get_status(mysql_conf_file=kwargs['mysql_conf_file']),
}

sys.stdout.write(str(opts[kwargs['command']]()) + '\n')
