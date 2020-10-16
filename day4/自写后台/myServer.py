# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/16

import socket

sk = socket.socket()

sk.bind(('127.0.0.1', 13000))
sk.listen()

while True:
    conn, addr = sk.accept()
    date = conn.recv(1024)
    print(date.decode('utf8'))

    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p>欢迎进入后台</p>
<select>
    <option>选项1</option>
    <option>选项2</option>
    <option>选项3</option>
</select>
</form>
</body>
</html>
    '''
    conn.sendall(('HTTP/1/1 200 OK\r\n%s' % html).encode('utf8'))