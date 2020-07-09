#coding:utf-8
"""
@author: mcfee
@description:闭包实践
@file: test_closure.py
@time: 2020/7/6 上午10:39
"""

def test():

    numbers=[] # 自由变量

    def add_numbers(number):
        c=3
        numbers.append(number)
        print(numbers)
    return add_numbers

a=test()
a(2)
a(3)
a(4)
print(a.__code__.co_freevars)
print(a.__code__.co_varnames)
print(a.__closure__[0].cell_contents)
