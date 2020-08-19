#coding:utf-8
"""
@author: mcfee
@description:
@file: property_class.py
@time: 2020/8/18 下午6:54
"""


class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


c=C()
c.x=222
print(c.x)