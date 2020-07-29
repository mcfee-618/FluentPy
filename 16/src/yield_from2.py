#coding:utf-8
"""
@author: mcfee
@description:
@file: test_yield_from2.py
@time: 2020/7/29 下午2:18
"""
import inspect
class Task:

    def __init__(self,gen):
        self.gen=gen

    def run(self):
        print(self.gen,inspect.getgeneratorstate(self.gen))
        yield from self.gen # yield from 把test2()这个生成器接收了


def test1():
    yield 2
    yield 3
    print(2)
    yield 4
    yield 5


def test2():
    yield from test1()

def test3(b):
    yield from b

# task= Task(test2())
# print(inspect.getgeneratorstate(task.run()))
# print(next(task.run()))
# print(next(task.run()))
# a= test3()
# print(next(a))
# print(next(a))
# task= Task(test2())
# a= task.run()
# print(type(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
task1 = test2() ### 必须要把生成器保存起来不然是不支持的
task2 = test3(task1)
task3 = test3(task1)
print(next(test3(task1)))
print(next(task1))
print(next(task1))
#print(next(test3(task1)))
