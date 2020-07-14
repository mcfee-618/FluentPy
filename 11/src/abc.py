# coding:utf-8
"""
@author: mcfee
@description:
@file: abc.py
@time: 2020/7/14 下午5:10
"""

import collections.abc

import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self):
        """从可迭代对象中添加元素。"""
        return 2

class Totoro(Tombola):

    def load(self):
        """从可迭代对象中添加元素。"""
        print(super().load())
        return 2

obj = Totoro()
#子类未实现方法会报错
#Can't instantiate abstract class Totoro with abstract methods load
obj.load()
print(Tombola.__subclasses__())