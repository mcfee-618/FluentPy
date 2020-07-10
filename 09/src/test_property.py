#coding:utf-8
"""
@author: mcfee
@description:
@file: test_property.py
@time: 2020/7/10 下午3:12
"""

class Person:

   x=3


p=Person()
print(dir(p))
p.x=22  # 为不存在的实例属性赋值，会新建实例属性，后面再访问会把同名类属性遮盖了
print(p.x)
