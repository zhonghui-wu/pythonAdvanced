# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/9/28

with open('./gbk编码.txt','r',encoding='gbk') as f:
    data = f.read()
with open('./utf8编码.txt','r',encoding='utf8') as f:
    data2 = f.read()
print(data+data2)

data3 = data2+data
def NewFile(name):
    with open(name,'w',encoding='utf8') as f:
        newData = f.write(data3)
        return newData
NewFile(input('请输入新名称:'))



#下面这种方法是不行的，因为两个txt文件编码不一样，写到同一个txt会变成两个编码格式组成的txt
# with open('./gbk编码.txt','rb') as f:
#     data = f.read()
# with open('./utf8编码.txt','rb') as f:
#     data2 = f.read()
# print(data+data2)
#
# data3 = data2+data
# def NewFile(name):
#     with open(name,'wb') as f:
#         newData = f.write(data3)
#         return newData
# NewFile(input('请输入新名称:'))
