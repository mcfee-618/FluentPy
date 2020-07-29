# coding:utf-8
"""
@author: mcfee
@description:
@file: simple_eventloop.py
@time: 2020/7/28 下午6:42
"""
from random import randint
import inspect
import collections
import time


class Future:
    def __init__(self, time):
        self.callback = None
        self.param = None
        self.time = time

    def add_done_callback(self, fn, param):
        self.callback = fn
        self.param = param

    def __call__(self, *args, **kwargs):
        print("开始执行future")
        self.callback(self.param)
        print("结束执行future")


class MyTask:
    def __init__(self, gen):
        self.generator = gen

    def __call__(self, *args, **kwargs):
        rs = None
        try:
            rs = next(self.generator)
        except StopIteration as e:
            pass
        else:
            return rs




class EventLoop:
    def __init__(self):
        self.pending_tasks = collections.deque()
        self.waiter_tasks = collections.deque()

    def run_until_complete(self, tasks):
        for task in tasks:
            self.pending_tasks.append(task)

    def run(self):
        while True:
            nwait = len(self.waiter_tasks)
            new_waiters = collections.deque()
            for i in range(nwait):
                task = self.waiter_tasks.popleft()
                if task.time <= time.time():
                    self.pending_tasks.append(task)
                else:
                    new_waiters.append(task)
            self.waiter_tasks = new_waiters
            ntodo = len(self.pending_tasks)
            for i in range(ntodo):
                task = self.pending_tasks.popleft()
                rs = task()
                if isinstance(rs, Future):
                    rs.add_done_callback(self.add_task, task)
                    self.waiter_tasks.append(rs)

            if len(self.pending_tasks)==0 and len(self.waiter_tasks)==0:
                break

    def add_task(self, task):
        self.pending_tasks.append(task)

    def remove_task(self, task):
        self.pending_tasks.remove(task)


eventloop = EventLoop()


def task1():
    print("task1-a")
    print("task1-c")
    yield from sleep(1)
    print("task1-b")
    print("task1-d")

def task2():
    print("task2-a")
    print("task2-c")
    yield from sleep(1)
    print("task2-b")
    print("task2-d")


    #exit()

def sleep(seconds):
    future = Future(seconds + time.time())
    yield future


task = MyTask(task1())
eventloop.add_task(task)
eventloop.add_task(MyTask(task2()))
eventloop.run()
