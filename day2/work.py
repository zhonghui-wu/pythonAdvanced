# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/12

'''
global用法：
    如果需要在函数内部改变函数外部的变量，就可以通过在函数内部声明变量为global变量。这样当程序运行至global变量便会替换外部的同名变量。
ps：
    name = '中卉'
    def test():
        global name
        name = 'zhonghui'
        return name

    print(name)
    test()
    pring(name)

执行完后的name就等于 zhonghui 了
'''

import uuid