# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/10

def foo():
    print('我是一个函数')
#函数名可以赋值给其他变量
# a = foo
# a()

# def foo():
#     print('我是一个函数')
# foo = 1
# print(foo)# = 1


# def test(a):
#     a()
#
# #函数名作为参数传递
# test(foo)


def bar():
    print('我是bar函数')

    def inner():
        print('我是inner函数')
#函数名作为返回值
    return inner

a = bar()
a()