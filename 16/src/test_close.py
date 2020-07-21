#coding:utf-8
"""
@author: mcfee
@description:
@file: test_close.py
@time: 2020/7/21 上午11:54
"""
import inspect

def gen():
    try:
        c=yield 2
    except GeneratorExit as e:
        # 收尾工作
        # GeneratorExit异常定义的初衷，是方便开发者在生成器对象调用结束后定义一些收尾的工作，如释放资源等
        print("release something")
    print(200)


a=gen()
print(next(a))
print(inspect.getgeneratorstate(a))
a.close()
print(inspect.getgeneratorstate(a))
