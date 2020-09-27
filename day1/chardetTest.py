# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/9/27

import chardet

#获取文件编码类型
def get_encoding(file):
    #二进制读取文件数据
    with open(file,'rb') as f:
        data = f.read()
        return chardet.detect(data)

enData = get_encoding('/Users/wuzhonghui/PycharmProjects/pythonAdvanced/a.txt')
print(enData)