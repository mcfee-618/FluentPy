#coding:utf-8
"""
@author: mcfee
@description:
@file: test_finalize.py
@time: 2020/7/9 下午3:26
"""
import weakref
class Object:
    pass

kenny = Object()
weakref.finalize(kenny, print, "You killed Kenny!")
# 使用 finalize 的主要好处在于它能更简便地注册回调函数，而无须保留所返回的终结器对象。
del kenny