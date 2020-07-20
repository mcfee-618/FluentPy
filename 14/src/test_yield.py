#coding:utf-8
"""
@author: mcfee
@description:
@file: test_yield.py
@time: 2020/7/20 下午3:06
"""
def gen():
    yield 2
    yield 3

a=gen()
print(a) #<generator object gen at 0x103d89d58>
print(next(a))
print(next(a))
#print(next(a))

