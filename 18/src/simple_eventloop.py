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
import socket, select


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
            print("结束任务")
        else:
            return rs


class EventLoop:
    def __init__(self):
        self.pending_tasks = collections.deque()
        self.waiter_tasks = collections.deque()
        self.read_list = []
        self.fd_callbacks = dict()

    def run_until_complete(self, tasks):
        for task in tasks:
            self.pending_tasks.append(task)

    def run(self):
        while True:
            # 文件描述符
            active_rfds, active_wfds, active_efds = select.select(self.read_list, [], [],1)
            for active_rfd in active_rfds:
                fd = active_rfd.fileno()
                callback = self.fd_callbacks[str(fd)]
                callback()
            # 额外逻辑
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
                    if rs.time != 0:
                        rs.add_done_callback(self.add_task, task)
                        self.waiter_tasks.append(rs)
                    else:
                        rs.add_done_callback(self.add_task, task)

            # if len(self.pending_tasks) == 0 and len(self.waiter_tasks) == 0:
            #     break

    def add_task(self, task):
        self.pending_tasks.append(task)

    def remove_task(self, task):
        self.pending_tasks.remove(task)

    def socket_get(self, ip, port):
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.setblocking(False)
        try:
            new_socket.connect((ip, port))
        except BlockingIOError as e:
            pass
        self.read_list.append(new_socket)
        fd = new_socket.fileno()
        future = Future(0)
        self.fd_callbacks[str(fd)] = future
        yield future
        try:
            value = new_socket.recv(100)
        except BlockingIOError as e:
            future = Future(0)
            self.fd_callbacks[str(fd)] = future
            yield future
            value = new_socket.recv(100)
        self.read_list.remove(new_socket)
        del self.fd_callbacks[str(fd)]
        return value


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


def task3():
    print("task3-a")
    print("task3-c")
    value= yield from eventloop.socket_get("127.0.0.1", 8097)
    print(value)
    print("task3-b")
    print("task3-d")


def async_socket(ip, port):
    eventloop.socket_get(ip, port)


def sleep(seconds):
    future = Future(seconds + time.time())
    yield future


task = MyTask(task1())
eventloop.add_task(task)
eventloop.add_task(MyTask(task2()))
eventloop.add_task(MyTask(task3()))
eventloop.run()
