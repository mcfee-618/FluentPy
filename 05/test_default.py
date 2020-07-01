#coding:utf-8
"""
@author: mcfee
@description:
@file: test_default.py
@time: 2020/7/1 下午5:22
"""
def test(c=2,d=3,h=5):
    pass

print(test.__defaults__)
print(dir(test.__code__))

