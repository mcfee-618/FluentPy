#coding:utf-8
"""
@author: mcfee
@description:
@file: server.py
@time: 2020/8/1 下午3:54
"""
import socket,time


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8097))
server.listen(10)
while True:
    new_socket,address=server.accept()
    print(address)
    time.sleep(2)
    new_socket.send(bytes("hello".encode("utf-8")))