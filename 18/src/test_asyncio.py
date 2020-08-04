#coding:utf-8
"""
@author: mcfee
@description:
@file: test_asyncio.py
@time: 2020/8/4 下午3:03
"""
import asyncio


async def test1():
    print(2)
    await asyncio.sleep(20)
    print(3)

async def test2():
    print(3)
    print(4)

event_loop = asyncio.get_event_loop()
task1=event_loop.create_task(test1())
task2=event_loop.create_task(test2())
event_loop.run_until_complete(asyncio.wait([task1,task2]))