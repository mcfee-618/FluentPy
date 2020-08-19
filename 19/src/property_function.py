#coding:utf-8
"""
@author: mcfee
@description:
@file: property_function.py
@time: 2020/8/18 下午5:49
"""

class Student:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        print('获取属性时执行的代码')
        return self._age

    @age.setter
    def age(self, age):
        print('设置属性时执行的代码')
        self._age = age

    @age.deleter
    def age(self):
        print('删除属性时执行的代码')
        del self._age


stu = Student()
print(stu.__dict__)
print(Student.__dict__) #  'age': <property object at 0x1040192c8>