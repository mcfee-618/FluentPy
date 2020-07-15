# coding:utf-8
"""
@author: mcfee
@description:
@file: test_extend2.py
@time: 2020/7/14 下午6:07
"""
import copy

class MRO:

    def parse(self, class_list_list):
        values = []
        while len(class_list_list) != 0:
            i = 0
            while i < len(class_list_list):
                current_class = class_list_list[i][0]
                flag = True
                for j, class_list in enumerate(class_list_list):
                    if j == i:
                        continue
                    for k, cls in enumerate(class_list):
                        if k != 0 and cls != current_class:
                            flag = False
                            break
                    if not flag:
                        break



