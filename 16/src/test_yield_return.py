#coding:utf-8
"""
@author: mcfee
@description:
@file: test_yield_return.py
@time: 2020/7/21 下午4:20
"""
import inspect

def gen():
    c=yield 2
    print(c)
    d=yield 3
    print(c,d)
    #  在 Python 3.3 之前，如果生成 器返回值，解释器会报句法错误。
    #  获取协程的返回值虽然要绕个圈子，但这是 PEP 380 定义的方式，当我们意识到这一点之后就说得通了：yield from 结构会在内部自动捕获 StopIteration 异常。
    return 1000


a=gen()
next(a)
print(a.send(22))
try:
    c=a.send(33)
    print("888")
except Exception as e:
    print(e.value)