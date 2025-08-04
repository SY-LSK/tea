#using_model/tea_compile.py
import else_package.color_console as color_console

def to_code(token):
    if token.type == 'function':
        if token.value == 'tout':
            return f'print({token.args})'
        if token.value == 'tin':
            return f'input({token.args})'
        # 新增对变量赋值的处理
        if token.value == 'var':
            return f'{token.args[0]} = {token.args[1]}'
    return ''