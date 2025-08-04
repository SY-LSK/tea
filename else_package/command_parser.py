#small_package/command_parser.py
import argparse

def parse_cmd():
    parser = argparse.ArgumentParser(description='Tea命令行')

    parser.add_argument('main_cmd',help='输入主命令的路径')
    parser.add_argument('-p','--path',help='输出文件的路径')

    return parser.parse_args()