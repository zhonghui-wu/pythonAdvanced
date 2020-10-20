# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/19

import paramiko

# 创建 SSH 对象
ssh = paramiko.SSHClient()

# 设置连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 远程主机 ip 地址，端口号， 在远程主机已经存在的用户名和密码
ssh.connect('192.168.2.138', 22, 'wuzhonghui', '123')

'''
# 发送命令
stdin, stdout, stderr = ssh.exec_command('ls')
# stdin1, stdout1, stderr1 = ssh.exec_command('pwd')  # 如果我运行两个这个，则是打开两个终端，各自发送命令
print(stdout.read().decode('utf8'))
# print(stdout1.read().decode('utf8'))
'''

# 将本地文件传输到远程机器
sftp = ssh.open_sftp()

# 第一个参数是本地文件路径，第二个是远程机器保存的路径
sftp.put('/Users/wuzhonghui/Downloads/Explo1t Dict.zip', '/home/wuzhonghui/Desktop/Explo1tDict.zip')

# 将远程机器上的文件传到本地，第一个参数是远程机器的文件路径，第二个参数是本地路径
# sftp.get('/home/wuzhonghui/Desktop/Explo1tDict.zip', '/Users/wuzhonghui/PycharmProjects/pythonAdvanced/day5/Explo1tDict.zip')
ssh.close()