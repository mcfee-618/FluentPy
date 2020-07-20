#coding:utf-8
"""
@author: mcfee
@description:
@file: test_generator.py
@time: 2020/7/20 下午4:56
"""

def gen():
    return (item for item in [1,2,3,4])

a=gen()
print(next(a))