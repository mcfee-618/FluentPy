#coding:utf-8
"""
@author: mcfee
@description:
@file: test_decorator.py
@time: 2020/7/6 下午12:02
"""

def d1(func):
    def inner(*args):
        print("d1")
        func(args)
    return inner


def d2(func):

    def inner(*args):
        print("d2")
        func()
    return inner

@d1
@d2
def test():
    print("22")

test()#f = d1(d2(f))