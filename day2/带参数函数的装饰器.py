# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/10

def bar(func):
    def inner(samething,a,b,c,d):
        func(samething,a,b,c,d)
        print('学习了一些新的知识')
    return inner

@bar
def foo(samething,a,b,c,d):
    print('正在做某事：',samething)


foo('看电视',1,2,3,4)