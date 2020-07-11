# coding:utf-8
"""
@author: mcfee
@description:
@file: test_slice.py
@time: 2020/7/10 下午3:12
"""
a = [1, 2, 3, 4]
print(a[1:-1])
print(type(a[1:-1]))


class Person:

    def __getitem__(self, item):
        print("222")
        return item


person = Person()
print(person[1:-1])  # slice(1, -1, None)
print(dir(slice))
print(slice(None, 10, 2).indices(5)) #长度为5的切片，start=none，end=10，步长为2
b=person[1:-1]
print(b)