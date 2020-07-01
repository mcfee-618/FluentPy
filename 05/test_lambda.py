#coding:utf-8
"""
@author: mcfee
@description:
@file: test_lambda.py
@time: 2020/7/1 下午5:00
"""

c=lambda x,y:x+y
# lambda 函数的定义体中不能赋值，也不能使用 while 和 try 等 Python 语句。
print(c(2,3))
