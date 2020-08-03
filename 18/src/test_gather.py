#coding:utf-8
"""
@author: mcfee
@description:
@file: test_gather.py
@time: 2020/8/3 下午6:00
"""
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print("Task {0}: Compute factorial({1})...".format(name,1))
        await asyncio.sleep(1)
        f *= i
    print("Task {name}: factorial({number}) = {f}".format(name=name,number=number,f=f))

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

eventloop =asyncio.get_event_loop()
eventloop.run_until_complete(main())