# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/15

'''服务端'''
import socket

# import sys

sk = socket.socket()

sk.bind(('0.0.0.0', 19000))
sk.listen()
print('start')

while True:
    cnn, addr = sk.accept()
    while True:
        receiveMsg = cnn.recv(1024)
        print(receiveMsg.decode('utf8'))
        if receiveMsg.decode('utf8') == 'q':
            # sys.exit()
            break
        msg = cnn.sendall(input('>>>').encode('utf8'))
        if msg == 'q':
            break

    break
