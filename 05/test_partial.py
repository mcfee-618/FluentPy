#coding:utf-8
"""
@author: mcfee
@description:
@file: test_partial.py
@time: 2020/7/1 下午6:42
"""
from functools import *
def pow(x,y):
    return x+y

def test1(*args):
    print(args)


pow1=partial(pow,x=2)
print(pow1(y=3))
print(test1(2,3,4,5))