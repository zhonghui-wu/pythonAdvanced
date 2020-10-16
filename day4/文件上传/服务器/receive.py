# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/15

import socket
import os


def get_file(sk_obj):
    """
    接收文件
    :param sk_obj:  socket对象
    :return: None
    """
    # 接收文件大小
    file_size = int(sk_obj.recv(1024).decode('utf8'))
    sk_obj.sendall(b'ok')
    # 接收文件名称
    file_name = sk_obj.recv(1024).decode('utf8')
    sk_obj.sendall(b'ok')

    # 接收文件内容
    with open(input('输入要保存的名称：') + '.jpg', 'wb') as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))  # 写入接收的内容
            file_size = file_size - 1024


sk = socket.socket()

sk.bind(('127.0.0.1', 13000))

sk.listen()

conn, addr = sk.accept()

get_file(conn)

conn.close()
