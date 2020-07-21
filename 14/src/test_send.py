#coding:utf-8
"""
@author: mcfee
@description:
@file: test_send.py
@time: 2020/7/20 下午3:06
"""

def yield_send():
    a = yield 2
    b = yield 3
    print(a,b)

obj = yield_send()
print(next(obj))
print(obj.send(95))
print(obj.send(4))