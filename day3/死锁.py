# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14
'''解决方法请看递归锁'''
import threading, time

lockA = threading.Lock()  # 面试官的锁
lockB = threading.Lock()  # 小明的锁

# 面试官
def foo1():
    lockA.acquire()  # 上锁
    print('请解释什么是死锁')
    time.sleep(1)

    lockB.acquire()  # 上锁
    print('发offer')
    time.sleep(1)

    lockA.release()
    lockB.release()

def foo2():
    lockB.acquire()  # 上锁
    print('请先给我发offer')
    time.sleep(1)

    lockA.acquire()  # 上锁
    print('解释什么是死锁')
    time.sleep(1)

    lockA.release()
    lockB.release()


t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()
