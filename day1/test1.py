# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/9/25

#将字符转为整数表示，只支持一个字
# print(ord('吴'))
#
#将整数转为字符
# print(chr(235567))

# a = 'abc'
# b = b'abc'
#
# print(type(a))
# print(type(b))

#str和bytes互转
# a = '的空间啊生机勃发哭吧哭吧'
# b = a.encode('utf8')
# print(b)
# print(b.decode('utf8'))


# with open('./a.txt','w',encoding='gb2312') as f:
#     f.write('写一行文字')

# with open('./a.txt','r',encoding='gb2312') as f:
#     data = f.read()
#     print(data)

#图片的复制
with open('./qq.png','rb') as f:#rb是二进制读
    data = f.read()
    # print(data)
with open('./qq2.png','wb') as f:#wb是二进制写
    f.write(data)