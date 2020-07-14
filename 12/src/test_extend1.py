#coding:utf-8
"""
@author: mcfee
@description:
@file: test_extend.py
@time: 2020/7/14 下午6:07
"""
class A:
    def pong(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):

    def pong(self):
        super().pong()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()

D().pong()
# Python 能区分 d.pong() 调用的是哪个方法，是因为 Python 会按照特定的顺序遍历继承图。
# 这个顺序叫方法解析顺序（Method Resolution Order，MRO）
C().pong()
print(D.__mro__)
