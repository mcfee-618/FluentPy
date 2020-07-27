#coding:utf-8
"""
@author: mcfee
@description:
@file: test_future.py
@time: 2020/7/27 下午3:43
"""
import requests
from concurrent import futures

def test():
    response = requests.get("http://www.baidu.com")
    return response.content
pool=futures.ThreadPoolExecutor(1)
future1=pool.submit(test) # 需要异步执行的函数
future1.result()
future2=pool.submit(test)
future3=pool.submit(test)
#An iterator over the given futures that yields each as it completes.
futures = futures.as_completed([future1,future2,future3])
for item in futures:
    print(item)

