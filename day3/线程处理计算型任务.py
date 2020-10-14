# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14

import threading,time

def foo():
    num = 0
    for i in range(10000000):
        num += 1

start_time = time.time()

#并发 总消耗时长 1.4901878833770752
t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=foo)
t1.start()
t2.start()
t1.join()
t2.join()

'''
#串行 总消耗时长 1.624964952468872
foo()
foo()
'''
end_time = time.time()

print('总消耗时长',end_time - start_time)