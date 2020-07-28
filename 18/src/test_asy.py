#coding:utf-8
"""
@author: mcfee
@description:
@file: test_asy.py
@time: 2020/7/28 下午3:20
"""
import asyncio

@asyncio.coroutine
def async1():
    print("async1-start")
    yield from asyncio.sleep(3)
    print("async1-end")

@asyncio.coroutine
def async2():
    print("async2-start")
    #yield from asyncio.sleep(4)
    print("async2-end")


@asyncio.coroutine
def async3():
    print("222")
    yield from async4()
    print("333")

@asyncio.coroutine
def async4():

    for i in range(10):
        pass
        #yield from test2()


def test2():
    return [22,33]
# The problem is that you can't just call existing synchronous code as if it was an asyncio.coroutine and get asynchronous behavior.
# yield from 必须是 asyncio.coroutine, or at least returns an asyncio.Future

event_loop = asyncio.get_event_loop()
future = asyncio.gather(async1(),async2(),async3(),async3())
print(type(async1()))
event_loop.run_until_complete(future)