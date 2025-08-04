#using_model/tea_use.py
import re
import sys

import using_model.tea_object as tea_object
import using_model.tea_constant as tea_constant
import using_model.tea_compile as tea_compile


def get_tea(file_path):
    word_list = []
    with open(file_path, 'r', encoding='UTF-8') as file:  
        for line in file:
            line = line.split(';')[0]
            word_list.append(re.split(r'([()''])',line)[:-1])
    return word_list

def tea_to_token(tea_list):
    token_list = []
    for line in tea_list:
        new_token = tea_object.to_token(line)
        token_list.append(new_token)
    return token_list

def token_to_code(token_list):
    code_list = []
    for token in token_list:
        code_list.append(tea_compile.to_code(token))
    return code_list

def write_py_file(py_file_path,token_list):
    errorline = 0
    with open(py_file_path, 'w', encoding='utf-8') as file:
        for line in token_list:
            file.write(line + '\n')