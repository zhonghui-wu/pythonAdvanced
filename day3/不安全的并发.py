# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14

import threading,time

balance = 500 # 账户余额
r = threading.Lock() # 声明一把锁
'''
这是一把同步锁
同步锁必须 上锁与解锁 相对应
如果上锁之后不解锁，再次上锁，代码会阻塞
如果解锁后再次解锁，代码会报错
'''
# 操作账户余额
def foo(num):
    # 声明全局变量。会改变原有的变量时要用 global
    global balance
    r.acquire() # 上锁
    # 将自己的余额放入自己的系统变量中
    user_balance = balance
    time.sleep(1)
    # 计算结果
    user_balance = user_balance + num
    # 将结果传递出去
    balance = user_balance
    r.release() # 解锁

# 消费300
t1 = threading.Thread(target=foo, args=[-300])
# 收入10000
t2 = threading.Thread(target=foo, args=[10000])

t1.start()
t2.start()

t1.join()
t2.join()

print('最终余额', balance)