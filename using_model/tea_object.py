#using_model/tea_object.py
import using_model.tea_constant as tea_constant


class token():
    def __init__(self,type,value,args):
        self.type = type
        self.value = value
        self.args = args

def to_token(code):
    new_token = ''
    if code[0] in tea_constant.function_list and code[1] == '(' and code[-1] == ')':
        new_token = token('function',code[0],','.join(code[2:-1]))
    return new_token