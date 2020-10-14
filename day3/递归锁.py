# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14
'''用于解决死锁的问题'''

import threading, time

lockR = threading.RLock()  # 递归锁
'''
递归锁内部维护着一把锁和一个计数器
每次上锁，计数器加一
每次解锁，计数器减一
计数器可以大于0，也可以等于0，不能小于0
'''

# 面试官
def foo1():
    lockR.acquire()  # 上锁
    print('请解释什么是死锁')
    time.sleep(1)

    lockR.acquire()  # 上锁
    print('发offer')
    time.sleep(1)

    lockR.release()
    lockR.release()

def foo2():
    lockR.acquire()  # 上锁
    print('请先给我发offer')
    time.sleep(1)

    lockR.acquire()  # 上锁
    print('解释什么是死锁')
    time.sleep(1)

    lockR.release()
    lockR.release()


t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()