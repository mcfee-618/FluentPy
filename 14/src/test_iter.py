#coding:utf-8
"""
@author: mcfee
@description:
@file: test_iter.py
@time: 2020/7/20 上午10:27
"""

class Persons:

    def __init__(self):
        self.values=[1,2,3,4,5]

    # def __iter__(self):
    #     yield 2
    #     yield 3

    def __getitem__(self, item):
        if item>4:
            raise StopIteration()
        return item


a=Persons()
for item in a:
    print(item)
