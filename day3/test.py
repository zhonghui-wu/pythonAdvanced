# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14

#这里考的是深浅拷贝和等号赋值，
L1 = [1, 2, 3]
L2 = [L1, 4, 5]
L3 = L2
L4 = L3.copy()#这里复制的L3是【【1，10，3】，4，5】
L1[1] = 10
L3[1] = 40
L4[2] = 50

print(L1)
print(L2)
print(L3)
print(L4)