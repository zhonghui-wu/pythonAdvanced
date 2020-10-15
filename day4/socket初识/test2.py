# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/15

'''客户端'''
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 19000))

while True:
    msg = sk.sendall(input('>>>').encode('utf8'))
    if msg == 'q':
        break
    receive = sk.recv(1024)
    print(receive.decode('utf8'))
    if receive == 'q':
        break

    break
