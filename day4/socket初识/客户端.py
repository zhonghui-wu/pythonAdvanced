# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/15

import socket
# 定义一个连接
sk = socket.socket()
# 发起连接，端口号要和服务端一致
sk.connect(('127.0.0.1', 13000))
# 发送数据
sk.sendall(input('>>>').encode('utf8'))
#接收数据
msg = sk.recv(1024)
print(msg.decode('utf8'))