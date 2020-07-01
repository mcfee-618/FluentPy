#coding:utf-8
"""
@author: mcfee
@description:
@file: test_callable.py
@time: 2020/7/1 下午5:10
"""
def test():
    print("test function")

def yield_function():
    yield 2
    yield 3


class A:
    pass

class B:

    def __call__(self, *args, **kwargs):
        pass

print(callable(test))
print(callable(A))
print(callable(B()))
print(callable(yield_function))