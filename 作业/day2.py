# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/20

# 要求编写装饰器，为 my_log、my_name、my_shopping_mall 函数加上认证的功能，要求登录成功一次，后续的函数都无需再输入用户名和密码
# 补充知识: token
#  token的意思是“令牌”，是服务端生成的一串字符串（这里我们可以随意指定一个字符串），作为客户端进行请求的一个标识。
#  当用户第一次登录后，服务器生成一个 token 并将此 token返回给客户端，以后客户端只需带上这个 token 来请求数据即可，无需再次带上
#  用户名和密码


import uuid

user_dict = {  # 存用户名和密码
    "user1": "123",
    "user2": "123",
}

token = None


def auth(func):
    def inner(*args, **kwargs):
        global token
        if token:  # token 有效
            func(*args, **kwargs)
        else:  # token 无效
            userName = input('请输入用户名>>>')
            userPwd = input('请输入密码>>>')

            if userName in user_dict and userPwd == user_dict[userName]:
                func(*args, **kwargs)
                token = str(uuid.uuid4())  # 生成一个随机字符串作为 token
            else:
                print('账号或密码错误')

    return inner


''' 
这个装饰器是让查看信息的时候显示用户输入的 userName
def auth1(func):
    userName = ''

    def inner(*args, **kwargs):
        global token
        global userName
        if token:  # token 有效
            func(userName)
        else:  # token 无效
            userName = input('请输入用户名>>>')
            userPwd = input('请输入密码>>>')

            if userName in user_dict and userPwd == user_dict[userName]:
                func(userName)
                token = str(uuid.uuid4())  # 生成一个随机字符串作为 token
            else:
                print('账号或密码错误')

    return inner
'''


@auth
def my_log():
    print('this is my_log')


@auth
def my_name(name):
    print('欢迎登陆', name)


@auth
def my_shopping_mall():
    print('商城购物')


while True:
    choose_num = input('\n\n1、查看日志\n2、我的信息\n3、我的商城\n请输入操作选项(输入 q 退出)>>>')
    if choose_num == 'q' or choose_num == 'Q':
        break
    elif choose_num == '1':
        my_log()
    elif choose_num == '2':
        my_name('张三')
    elif choose_num == '3':
        my_shopping_mall()
    else:
        print('输入不合法')
