#coding:utf-8
"""
@author: mcfee
@description:装饰器入门
@file: test_simple_decorator.py
@time: 2020/7/3 下午6:47
"""
from dis import dis
c=2

def test():
    print(c)
    #c=4
    print(c)
#编译函数的定义体时，它判断c是局部变量，因为在函数中给它赋值了。生成的字节码证实了这种判断，Python
#会尝试从本地环境获取 c 。

dis(test)