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

print(uuid.uuid1()) #等于  5269e1c0-0c76-11eb-ba67-8c8590f124be
print(uuid.uuid4()) #随机数生成的
print(uuid.uuid3(uuid.NAMESPACE_DNS,'test')) #等于  45a113ac-c7f2-30b0-90a5-a399ab912716
print(uuid.uuid5(uuid.NAMESPACE_DNS,'test1')) #等于  86e3aed3-1553-5d23-8d61-2286215e65f1
