#coding:utf-8
"""
@author: mcfee
@description:
@file: test_yield.py
@time: 2020/7/21 上午11:01
"""
import inspect

def gen():
    c=yield 2
    print(c)
    d=yield 3
    print(c,d)

a=gen()
print(inspect.getgeneratorstate(a)) # 处于created状态不能调用send，一般需要先调用next，必须调用send需要传入None
next(a) # 预激协程
print(inspect.getgeneratorstate(a))
a.send(10)
print(inspect.getgeneratorstate(a))
try:
    a.send(20)
except Exception as e:
    pass
print(inspect.getgeneratorstate(a))


## 使用协程之前必须预激，可是这一步容易忘记。

