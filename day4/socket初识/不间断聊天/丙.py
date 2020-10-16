# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/16

import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 13000))

while True:
    data = '用户丙：' + input('>>>')
    sk.sendall(data.encode('utf8'))

    msg = sk.recv(1024)
    print(msg.decode('utf8'))