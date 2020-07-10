#coding:utf-8
"""
@author: mcfee
@description:
@file: test_method.py
@time: 2020/7/10 下午1:52
"""
class Person:

    @staticmethod
    def test1(*args):
        print(args)

    @classmethod
    def test2(*args):
        print(args)

Person.test1(2)
Person.test2(2)

# (2,)
# (<class '__main__.Person'>, 2)