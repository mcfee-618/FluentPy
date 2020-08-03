#coding:utf-8
"""
@author: mcfee
@description:
@file: test_coroutine.py
@time: 2020/8/3 下午5:43
"""
import asyncio

@asyncio.coroutine
def test1():
    print(2)


print(asyncio.iscoroutine(test1()))
print(asyncio.iscoroutinefunction(test1))