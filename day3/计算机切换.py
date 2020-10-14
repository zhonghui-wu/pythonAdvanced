# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/13

import threading,time

def foo(something,num):
    for i in range(num):
        print('cpu正在',something)
        time.sleep(1)

#创建线程实例，target 指向任务函数，args 为 target 指向函数传参
t1 = threading.Thread(target=foo, args=('听音乐',2))
t2 = threading.Thread(target=foo, args=('看电影',5))

#启动线程
t1.start()
t2.start()