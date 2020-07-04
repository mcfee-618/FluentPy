#coding:utf-8
"""
@author: mcfee
@description:装饰器入门
@file: test_simple_decorator.py
@time: 2020/7/3 下午6:47
"""


def test(func):
    print("xxx")

    def inner(*args,**kwargs):
        print("fun before")
        print(func.__name__)
        func(*args,**kwargs)
        print("fun after")
    return inner

@test
def add(x,y):
    print("result is {0}".format(x+y))

add(2,3)
