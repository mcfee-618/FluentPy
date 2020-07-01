#coding:utf-8
"""
@author: mcfee
@description:
@file: test_function.py
@time: 2020/7/1 下午4:23
"""
def test(x,y):
    """
    :param x:
    :param y:
    :return:
    """
    return x+y

print(test) # function类型
print(dir(test))
print(test.__doc__) # _doc__ 是函数对象众多属性中的一个