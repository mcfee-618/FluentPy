#coding:utf-8
"""
@author: mcfee
@description:
@file: test_with.py
@time: 2020/7/24 下午2:53
"""
class Resource:

    def __enter__(self):
        print("进入上下文")

    # exc_type：异常类型
    # exc_val：异常值
    # exc_tb：异常的错误栈信息
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_val)
        print(exc_type)
        print("退出上下文")
        #return  True
        #在__exit__里返回 True（没有return就默认为return False），就相当于告诉Python解释器，这个异常我们已经捕获了，不需要再往外抛了。


with Resource() as r:
    pass
    #raise Exception("123")
