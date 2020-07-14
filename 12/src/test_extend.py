#coding:utf-8
"""
@author: mcfee
@description:
@file: test_extend.py
@time: 2020/7/14 下午6:07
"""
class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()

D().ping()
