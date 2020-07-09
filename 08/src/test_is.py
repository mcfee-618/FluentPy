#coding:utf-8
"""
@author: mcfee
@description:测试is和==
@file: test_is.py
@time: 2020/7/9 上午10:31
"""
class Person:

    def __init__(self):
        self.name=22

    def __eq__(self, other):
        return self.name==other.name

p1=Person()
p2=Person()
print(p1 is p2)
print(p1==p2)