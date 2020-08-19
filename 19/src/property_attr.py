#coding:utf-8
"""
@author: mcfee
@description:
@file: property_attr.py
@time: 2020/8/18 下午6:04
"""
class A:

    def __init__(self):
        self._age=None
        self.age=20

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        print('设置属性时执行的代码')
        self._age=age

    @age.deleter
    def age(self):
        print('删除属性时执行的代码')
        del self._age



a = A()
a.age=222
print(a.age)


