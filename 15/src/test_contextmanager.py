#coding:utf-8
"""
@author: mcfee
@description:
@file: test_contextmanager.py
@time: 2020/7/24 下午3:30
"""
import contextlib

@contextlib.contextmanager
def context():
    print("enter")
    try:
        a = yield 2
        #而yield之前的代码，就相当于__enter__里的内容。yield 之后的代码，就相当于__exit__里的内容。
    except Exception as e:
        print(e)
    finally:
        print("exit")


with context() as w:
    print(w)
    raise  Exception("222")
