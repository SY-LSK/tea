import os
import pathlib
import runpy
import sys

import using_model.tea_use as tea_use
import else_package.command_parser as command_parser
import else_package.color_console as color_console

def main():
    cmd_args = command_parser.parse_cmd()
    if cmd_args.main_cmd == 'run':
        if cmd_args.path:
            run(cmd_args.path)
        else:
            color_console.color_print('Tea:命令使用错误','red')
            sys.exit()
    else:
        color_console.color_print('Tea:命令使用错误','red')

def run(file_path):
    tea_file_path = file_path

    if not pathlib.Path(tea_file_path).suffix == '.tea':
        color_console.color_print('Tea:文件后缀名错误','red')
        sys.exit()

    tea_code = tea_use.get_tea(tea_file_path)
    token_list = tea_use.tea_to_token(tea_code)
    code_list = tea_use.token_to_code(token_list)

    compiled_file_name = f'{pathlib.Path(tea_file_path).stem}.py'
    tea_use.write_py_file(compiled_file_name,code_list)

    print('Tea:编译完成')
    print('Tea:运行中')
    try:
        runpy.run_path(compiled_file_name)
    except Exception as e:
        color_console.color_print(f'Tea运行错误:\n{e}','yellow')
        sys.exit()
    print('Tea:运行完成')
    os.remove(compiled_file_name)
    sys.exit()


if __name__ == '__main__':
    main()