# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14

import threading,time

a = []

def foo():
    while True:
        a.append('1')
        print('生产啦一个数据')
        time.sleep(1)

t1 = threading.Thread(target=foo)

# 设置t1守护线程，必须在 start 之前设置
# 作用就是在主线程想要退出进程的时候，不需要等待自己运行结束，直接退出就行了
# 默认是： 主从子 ，守护线程是： 子从主
t1.setDaemon(True)
t1.start()

for i in range(20):
    if a:
        a.remove('1')
        print('消耗啦一个数据')
    time.sleep(1)

print('不在需要数据啦')

