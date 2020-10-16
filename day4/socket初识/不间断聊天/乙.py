# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/16

import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 14000))

while True:
    # 开始聊天
    data = '用户乙：' + input('>>>')
    sk.sendall(data.encode('utf8'))

    # 接收信息
    msg = sk.recv(1024)
    print(msg.decode('utf8'))