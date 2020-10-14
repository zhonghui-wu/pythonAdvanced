# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14

'''
io : 需要等待类型的任务称为io任务.接口任务也属于io任务
'''

import threading,time

def foo(something):
    print(something)
    time.sleep(1)

start_time = time.time()

#创建实例线程
t1 = threading.Thread(target=foo, args=('磁盘写入100M数据',))
t2 = threading.Thread(target=foo, args=('cpu去做其他事',))

#启动线程,加阻塞后的执行时间为 1.0034592151641846
t1.start()
t2.start()

#在子线程完成运行之前，这个自线程的主线程将一直被阻塞
#不加阻塞时，会主线程运行结束了就结束了，执行时间为 0.000347137451171875
t1.join()
t2.join()

'''
执行时间为 2.006787061691284
foo('磁盘写入100M数据')
foo('cpu去做其他事')
'''
end_time = time.time()

print('执行时间为',end_time - start_time)
