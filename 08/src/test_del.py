#coding:utf-8
"""
@author: mcfee
@description:
@file: test_del.py
@time: 2020/7/9 上午11:52
"""
class Person:

    def __del__(self):
        print("del对象")

p1=Person()
P1=Person()
