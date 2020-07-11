# coding:utf-8
"""
@author: mcfee
@description:
@file: test_slice1.py
@time: 2020/7/10 下午3:12
"""
class Vector:

    def __init__(self,values):
        self.__values=values
    def __len__(self):
        return len(self.__values)
    def __getitem__(self, item): #生成切片会调用这个方法
        print(item)
        if isinstance(item,slice):
            return self.__values[item]
        else:
            return self.__values[item]
vector=Vector([1,2,3,4])
print(vector[2])
print(vector[1:-1])


