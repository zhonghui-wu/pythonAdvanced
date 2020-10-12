# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/9/28

import os
#相当于打开了终端输入括号里面的命令
#阻塞式调用：调用的外部程序没有推出时，python程序会一直停留在这里
#直到调用的外部程序退出，才会接着往下执行
# after = os.system('ifconfig')

#最后打印出来的0是程序结束时候的打印
# print(after)


# import subprocess
#也是阻塞式调用，且是返回的是字节
# after = subprocess.check_output('ifconfig')
#
# print(after.decode('utf8'))


from subprocess import Popen,PIPE
#输出重定向
# child = Popen('ifconfig',stdout=PIPE)
#
# output,err = child.communicate()
# print(output)

'''Popen函数正确传参方法：Popen(（'python3'，'ioTest.py'）, stdout=PIPE,stdin=PIPE, encoding='utf-8')'''
#输入重定向
child = Popen(('python3','ioTest.py'), stdout=PIPE,stdin=PIPE, encoding='utf-8')#stdout输出，stdin输入，Mac端要同时有这两个参数

output, err = child.communicate("q\nn")
print(output)

# child = Popen('python3 ioTest.py', stdout=PIPE, encoding='utf-8',shell=True)
# output,err = child.communicate('我\n是')
# print(output)



