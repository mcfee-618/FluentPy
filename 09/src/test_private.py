#coding:utf-8
"""
@author: mcfee
@description:
@file: test_private.py
@time: 2020/7/10 下午2:09
"""
class Point:

    def __init__(self):
        self.__x=2 # _Point__x, _Point__y
        self.__y=3

p=Point()
print(dir(p))