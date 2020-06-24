#coding:utf-8
"""
@author: mcfee
@description:字典推导
@file: test_dict.py
@time: 2020/6/24 上午11:05
"""
import collections

list1=[1,2,3,4,5]
print({str(item):"" for item in list1}) # 字典推导表达式


class MyDict(dict):
    def __missing__(self, key):
        return 22

a= MyDict()
print(a[22]) #找不到调用__missing__方法