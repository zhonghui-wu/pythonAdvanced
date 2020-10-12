# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/10

class Foo:

    @classmethod  #把函数变成类方法，保存在类当中，由类直接调用
    def foo(cls):
        print(123)

Foo.foo()