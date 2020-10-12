# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/10

def bar(func):
    def inner():
        func()
        #此处省略一系列神奇操作
        print('成功利用摄像头查看到手机壳颜色')
        print("成功修改ui界面")
    return inner
# print(foo())
# foo = bar(foo)
# print(foo)
# foo()

@bar#等于foo = bar(foo)
def foo():
#此处省略一堆操作
    print('事情干完了')

#开放封闭原则：允许扩展现有代码，但是静止修改已有功能代码

foo()