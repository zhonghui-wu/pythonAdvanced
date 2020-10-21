# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/21

import socket
name = 'Nathaniel'  # 定客户端的名称


def handleData(data):
    """
    将消息处理为特定格式
    :param data: 消息正文
    :return: 处理后的消息
    """
    # 先处理消息第二部分
    if data == 'Nathaniel':
        dataType = '1'
    else:
        dataType = '2'

    # 处理消息的第一部分
    strLen = len(data)
    if len(str(strLen)) < 4:
        dataLen = '0'*(4 - len(str(strLen))) + str(strLen)  # '0'* 5 的话就等于 00000
    else:
        dataLen = str(strLen)

    return '|'.join([dataLen, dataType, data])


# if __name__ == '__main__':
#     rte = handleData('哈哈')
#     print(rte)
sk = socket.socket()
sk.connect(('127.0.0.1', 13000))

# 先告诉服务端自己的姓名
sk.sendall(handleData(name).encode('utf8'))
sk.recv(1024)

while True:
    # 发信息
    inp = input('>>>')
    sk.sendall(handleData(inp).encode('utf8'))

    if inp == 'q':
        break

    # 收消息
    serverData = sk.recv(1024).decode('utf8')
    print(serverData)

