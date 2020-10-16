# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/16

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('开始聊天')

        while True:
            # 接收信息
            receive = self.request.recv(1024)  # 等于 conn.recv(1024)
            print(receive.decode('utf8'))

            # 发送信息
            self.request.sendall(input().encode('utf8'))


server = socketserver.ThreadingTCPServer(('127.0.0.1', 13000), MyServer)
print('上线了')
server.serve_forever()  # 启动服务
