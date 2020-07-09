#coding:utf-8
"""
@author: mcfee
@description:
@file: test_weakref.py
@time: 2020/7/9 下午2:35
"""
import weakref
import sys

a={2,3,4}
print(sys.getrefcount(a))
b=weakref.ref(a)
print(sys.getrefcount(a))
print(b)
print(b())
a=None
print(b)
print(b()) #对象不存在了，所以 wref() 返回 None


class MyList(list):
    """list的子类，实例可以作为弱引用的目标"""

a_list = MyList(range(10))

# a_list可以作为弱引用的目标
wref_to_a_list = weakref.ref(a_list)
#wref_to_a_list = weakref.ref([])