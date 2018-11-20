# coding:utf-8
import argparse, sys
import mission_planning

parser = argparse.ArgumentParser(description='Get Oracle process statistics with proto instance.',
                                 usage='hadoop fs -text xxx.pb.snappy | ./model_debug --model=xxxx --ps=xxxxx [options]')
subparsers = parser.add_subparsers(dest='command')
opts = {}
subp_ = subparsers.add_parser("create_mission")
opts['create_mission'] = lambda input_: create_mission(input_)
subp_.add_argument('-input')
subp_ = subparsers.add_parser("add_data")
subp_.add_argument('-input')
subp_ = subparsers.add_parser("get_main_ui_display")
subp_ = subparsers.add_parser("get_mission_planning_res")
kwargs = vars(parser.parse_args())

opts = {
    'create_mission': lambda: mission_planning.create_mission(kwargs['input']),
    'add_data': lambda: mission_planning.add_data(kwargs['input']),
    'get_main_ui_display': lambda: mission_planning.get_main_ui_display(),
    'get_mission_planning_res': lambda: mission_planning.get_mission_planning_res()
}

sys.stdout.write(str(opts[kwargs['command']]()) + '\n')
