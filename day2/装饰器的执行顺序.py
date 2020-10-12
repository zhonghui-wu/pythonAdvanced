# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/10

'''
装饰器的执行顺序
'''

def bar1(func):
    def inner():
        func()
        print(1)
    return inner

def bar3(func):
    def inner():
        func()
        print(3)
    return inner

def bar2(func):
    def inner():
        func()
        print(2)
    return inner

def bar4(func):
    def inner():
        func()
        print(4)
    return inner

#装饰器的执行方式是：：1，2，4，3。从下往上的
@bar3 #inner3
@bar4 #inner4
@bar2 #inner2
@bar1 #inner1
def foo1():
    print('我是foo')

foo1()#foo1函数只会被调用一次