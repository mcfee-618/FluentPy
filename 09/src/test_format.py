#coding:utf-8
"""
@author: mcfee
@description:
@file: test_format.py
@time: 2020/7/10 下午1:58
"""

print("{0}".format("2")) # 设置指定位置

print("{:.2f},{:.2f}".format(3.1415926,888.7676767)) # 数字格式化

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com")) # 命名格式化

# https://www.runoob.com/python/att-string-format.html