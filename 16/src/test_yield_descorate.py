#coding:utf-8
"""
@author: mcfee
@description:
@file: test_yield_descorate.py
@time: 2020/7/21 上午11:17
"""
import inspect
from functools import wraps

# 预激协程的装饰器
def decorator(func):

    @wraps(func)
    def inner():
        gen = func()
        next(gen)
        return gen

    return inner

@decorator
def gen():
    c=yield 2
    print(c)
    d=yield 3
    print(c,d)


a=gen()
print(inspect.getgeneratorstate(a))
print(a.send(22))


