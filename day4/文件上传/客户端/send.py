# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/16

import socket, os

list = ['/Users/wuzhonghui/PycharmProjects/pythonAdvanced/day4/文件上传/客户端/WechatIMG.png',
        '/Users/wuzhonghui/PycharmProjects/pythonAdvanced/day4/文件上传/客户端/123.jpg']

def post_file(sk_obj, file_path):
    """
    发送文件
    :param sk_obj: socket对象
    :param file_path: 文件路径
    :return: None
    """
    # 发送文件大小
    file_size = os.stat(file_path).st_size  # 获取文件大小
    file_size = str(file_size)  # 将 int 转为 str
    file_size = file_size.encode('utf8')  # 将 str 转为 bytes
    sk_obj.sendall(file_size)

    # 发送文件名称
    # os.path.split(file_path)[1] 是将上方的地址分割成两部分，
    # 第二部分将就是文件名称及格式
    sk_obj.sendall(os.path.split(file_path)[1].encode('utf8'))
    sk_obj.recv(1024)

    # 发送文件内容
    file_size = os.stat(file_path).st_size  # 重新获取，得到 int 型
    with open(file_path, 'rb') as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))  # 发送读取的内容
            file_size = file_size - 1024


sk = socket.socket()

sk.connect(('127.0.0.1', 13000))

post_file(sk, r'/Users/wuzhonghui/PycharmProjects/pythonAdvanced/day4/文件上传/客户端/123.jpg')

sk.close()
