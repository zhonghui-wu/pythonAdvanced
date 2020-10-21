# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/20
"""
# 实现一个简单的客服聊天系统。
# 客服中心是tcp服务端程序
# 客户使用tcp客户端程序。

# 服务端程序
# 先运行， 绑定本机一个ip地址， 等待客户端系统连接上来 。
# 客户端程序有一个命令行参数， 表示客户的名字
# 连接成功后，  客户端发送给服务端第一个消息
# 必须告诉客服中心，用户的名字
# 一个客户连接后，别的客户不能连接， 等到前面的客户断开连接后，才能连上。
# 客户端和服务端都是手动在终端输入信息，发送消息后，必须等待接受到对方的消息才能发送下一个消息。
# 我们定义消息的格式如下：
# 0008 | 1 | nickname
# 用竖线隔开3部分的字段，分别表示消息长度、 消息类型 、消息内容
# 前面字段是4个字节的字符串，比如'0008'，其内容是数字，表示消息的长度， 不足4个字节前面补零。
# 注意长度是整个消息内容的长度，包括消息头部和消息体
# 后面用竖线隔开的字段，是1个字节的字符串，是消息类型，其内容是数字，1表示客户昵称， 2表示普通消息,前面两个字段合起来
# 0008 | 1 |  ， 可以看成是一个消息的头部， nickname是消息体
# 再后面用竖线隔开的字段是消息内容，其长度等于前面消息长度字段指明的长度减去消息头部长度 （也就是7个字节）
# 服务端程序在下面, 大家参考服务端程序的实现，开发客户端程序和服务端进行通讯

"""

import socket

name = 'server'  # 定义一个名称
def handleData(data):
    """
    将消息处理为特定格式
    :param data: 消息正文
    :return: 处理后的消息
    """
    # 先处理消息第二部分
    if data == 'server':
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
sk.bind(('127.0.0.1', 13000))
sk.listen()

while True:
    conn, addr = sk.accept()
    clienName = conn.recv(1024).decode('utf8')
    print('客户端身份：', clienName)
    conn.sendall(b'ok')

    while True:
        clienData = conn.recv(1024).decode('utf8')
        print(clienData)
        if clienData[7] == 'q':
            break

        # 发消息
        serverDate = input('>>>')
        conn.sendall(handleData(serverDate).encode('utf8'))
        if serverDate == 'q':
            break
    conn.close()
