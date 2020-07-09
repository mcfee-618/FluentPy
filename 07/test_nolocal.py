# coding:utf-8
"""
@author: mcfee
@description:
@file: test_nolocal.py
@time: 2020/7/6 上午10:54
"""


def test():
    count = 0  # 自由变量

    def add_numbers(number):
        #nonlocal count
        count += number
        """
        在Python中，对于一个不可变数据类型比如上述示例中的count，count += 1
        和count = count + 1是等效的，averager的定义体中为count赋值了，这会把count变成局部变量
        """
        print(count)
    return add_numbers

a = test()
a(2)
