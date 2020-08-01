#coding:utf-8
"""
@author: mcfee
@description:
@file: debug1.py.py
@time: 2020/7/29 下午5:44
"""
import pdb

def test(x):
    x+=1
    print(x)

a = "a string"
b= "b string"
pdb.set_trace() #pdb.set_trace()，就可以设置一个断点,进入pdb调试环境，
print("next step1")
test(2)
print("next step2")
