#coding:utf-8
"""
@author: mcfee
@description:
@file: test_lru.py
@time: 2020/7/6 上午11:32
"""
import functools



@functools.lru_cache() # ➊
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))


# functools.lru_cache 是非常实用的装饰器，
# 它实现了备忘（memoization）功能。这是一项优化技术，它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。