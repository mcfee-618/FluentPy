#coding:utf-8
"""
@author: mcfee
@description:
@file: test_package.py
@time: 2020/7/2 下午3:20
"""
def test(*args):
    print(args) #拆包
    print(*args) #装包


test(1,2,3,4,5)
