#coding:utf-8
"""
@author: mcfee
@description:
@file: test_extend2.py
@time: 2020/7/14 下午6:07
"""
class p1:
    def __init__(self,value):
        self.value = value
class p2(p1):
    def __init__(self,key):
        super().__init__(key)
        self.key = key

obj=p2(3)
print(obj.key)
print(obj.value)