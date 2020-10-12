# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/9

'''
作用域是程序运行时变量可被访问的范围
    定义在函数内的变量是局部变量
    定义在函数最外层的是全局变量
'''

#全局作用域
g = 11111

# L (Local) : 局部作用域
def ha():
    c = 1

    def foo():#  E (enclosing) 嵌套作用域
        a = 'hello world'

        def bar():# L (Local) : 局部作用域
            b = 'hello python'
            print(a)
            print(g)
        print(b)
        print(g)
    print(g)
print(g)
