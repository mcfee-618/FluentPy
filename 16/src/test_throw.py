#coding:utf-8
"""
@author: mcfee
@description:
@file: test_throw.py
@time: 2020/7/21 上午11:50
"""

import inspect

def gen():
    try:
        c=yield 2
    except ZeroDivisionError as e:
        print("get exception")
    print(200)
    d=yield 3
    print(d)
try:
    a=gen()
    print(next(a))
    print(a.throw(Exception()))

except Exception as e:
    pass
print(inspect.getgeneratorstate(a))
