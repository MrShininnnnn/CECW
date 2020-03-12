#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Shining'
__email__ = 'mrshininnnnn@gmail.com'

# dependency
import json

# helper functions
# to read data from .txt file
def read_txt(path: str) -> list:
    with open(path, 'r') as f:
        return f.read().splitlines()

# to save data as .txt file
def save_txt(path: str, content: list):
    with open(path, 'w') as f:
        for seq in content:
            f.write(seq)
            f.write('\n')
        f.close()

# to save data as .json file
def save_json(path: str, data_dict: dict):
    with open(path, 'w') as f:
        json.dump(data_dict, f, ensure_ascii=False)

# to add primitive rules
def add_primitive_rule(src_seq: list, tar_seq: list, src_list: list, tar_list: list) -> tuple:
    src_list.append(src_seq)
    tar_list.append(tar_seq)
    return src_list, tar_list
