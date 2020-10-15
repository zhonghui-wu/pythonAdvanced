# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/15

import socket
# 创建连接
sk = socket.socket()
# 绑定ip和端口
sk.bind(('0.0.0.0', 13000))
# 监听端口
sk.listen()
print('开启服务')
# 等待传入连接，阻塞进程，传入后返回ip和端口
cnn, addr = sk.accept()
print('客户端地址为',addr)
# 接收数据大小设置及以utf8解码
receiveMsg = cnn.recv(1024)
print(receiveMsg.decode('utf8'))
# 发送数据
cnn.sendall(input('>>>').encode('utf8'))

