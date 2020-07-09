#coding:utf-8
"""
@author: mcfee
@description:
@file: test_param.py
@time: 2020/7/9 上午11:35
"""
class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):
        #函数的默认值是在定义函数时计算(通常是加载模块时)，因此默认值变成了函数的对象属性。
        passengers.append(2)
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

h1=HauntedBus([22])
print(h1.passengers)
h2=HauntedBus()
print(h2.passengers)