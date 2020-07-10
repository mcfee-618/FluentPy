#coding:utf-8
"""
@author: mcfee
@description:
@file: test_slot.py
@time: 2020/7/10 下午2:56
"""
# class definition
class Bar(object):
  def __init__(self, a):
    self.a = a

class BarSlotted(object):
  __slots__ = "a",
  def __init__(self, a):
    self.a = a

# create class instance
bar = Bar(1)
bar_slotted = BarSlotted(1)
print(dir(bar))
print(dir(bar_slotted)) # slotted_bar并没有__dict__而bar却含有__dict__

## pympler是一个开发工具，用于测量、监视和分析 运行的python应用程序中python对象的内存行为。
from pympler import asizeof
print(asizeof.asizeof(bar))
print(asizeof.asizeof(bar_slotted))
bar_slotted.c=2