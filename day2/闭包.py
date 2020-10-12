# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/10

#在一个内部函数里面，对在外部作用域（不能是全局作用域）的变量进行调用
#那么这个内部函数酒被称之为闭包
def outer():
    x = 10
    def inner():
        print(x)
    return inner

outer()()#可以拆成下面两行

a = outer() # 等于a = inner
a() #等于inner()