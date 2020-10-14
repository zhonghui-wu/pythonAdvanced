# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14

import threading,time

def foo():
    time.sleep(3)
    print('阳光明媚')

t1 = threading.Thread(target=foo)
t1.start()
t1.join() #再线程 t1 结束之前，阻塞主线程，不让继续往下运行

print('结束啦')#不加入join函数时，是先执行 '结束啦' 再执行 '阳光明媚' 的
