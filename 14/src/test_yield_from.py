#coding:utf-8
"""
@author: mcfee
@description:
@file: test_yield_from.py
@time: 2020/7/20 下午5:42
"""
def gen():
    sum=0
    for i in range(4):
        sum += yield i
        print(sum)


def gen1():
    a=gen()
    yield from a


a=gen1()
print(next(a))
a.send(2)
c=a.send(5)
print(c)