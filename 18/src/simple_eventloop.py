# coding:utf-8
"""
@author: mcfee
@description:
@file: simple_eventloop.py
@time: 2020/7/28 下午6:42
"""
from random import randint


class EventLoop:
    def __init__(self):
        # 待办事件列表，类似于收件箱，就是上图中的Task Queue，里面的task就是API
        self.events_to_listen = []
        # 当前可执行任务列表，单线程主要执行的队列
        self.events_to_process = []

        self.callbacks = {}
        self.timeout = 5

    def register_event(self, event, callback):
        self.events_to_listen.append(event)
        self.callbacks[event] = callback

    def unregister_event(self, event):
        self.events_to_listen.remove(event)
        del self.callbacks[event]

    # 根据超时时间，从队列里面找出超时的事件
    def poll_events(self):
        self.events_to_process = []

        for event in self.events_to_listen:
            # 如果还不到检查时间，就再等等
            if event.timeout < self.timeout:
                event.timeout += 1
            else:
                self.events_to_process.append(event)

    def _process_events(self, events):
        for event in events:
            # 模拟执行过程中可能会阻塞
            if randint(0, 1):
                self.callbacks[event]()
                self.unregister_event(event)
                # 如果阻塞了就不执行，同时将超时时间降低，放在待执行下次再检查
            else:
                event.timeout -= 2

    def start_loop(self):
        # pythontutor不支持无限循环的方式
        # while True:
        while True:
            self.poll_events()
            self._process_events(self.events_to_process)


class Event():
    def __init__(self, timeout, callback):
        self.timeout = timeout
        self.callback = callback

    def process(self):
        print('An Event is processed:', self.timeout)


def call_back():
    print('this is call_back')


loop = EventLoop()
for item in range(1, 4):
    timeout = randint(0, 6)
    event = Event(timeout, call_back)
    loop.register_event(event, call_back)
loop.start_loop()
