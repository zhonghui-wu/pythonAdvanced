# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/12

'''
字段
    1.普通字段，保存在对象里面，执行的时候只能通过对象调用
    2.静态字段，保存在类里面，执行的时候可以通过对象调用也可以通过类调用
'''

# class Foo:
#     name = '这是静态字段'
#     def __init__(self):
#         self.age = '这是普通字段'
#
# obj1 = Foo()
# obj2 = Foo()
# #obj1和obj2的位置不一样，所以他们是不一样的
# print(obj1)



'''
方法
    1.普通方法，保存在类里面，由对象调用
    2.静态方法，保存在类里面，可以通过类调用，也可以通过对象调用
    3.类  方法，保存在类里面，可以通过类调用，也可以通过对象调用
'''

# class Foo:
#     name = '这是静态字段'
#     def foo(self):
#         print(self.name)
#         print('这是普通方法')
#
#     @staticmethod
#     def foo1():
#         #print(name)静态方法不能调用静态字段
#         print('这是静态方法')
#
#     @classmethod
#     def foo2(cls):
#         print(cls.name)
#         print('这是类方法')
#
# #类方法，保存在类里面，由类直接调用，无需实例话
# Foo.foo2()
#
# #静态方法，保存在类里面，由类直接调用，无需实例话
# Foo.foo1()
#
# #普通方法，保存在类里面，只能由对象调用
# obj = Foo()
# obj.foo()


'''
属性   就是不加括号也能执行的方法
定义时，在普通方法上加一个装饰器
定义时，属性只有一个self参数
调用的时候，不用加括号
    方法的调用形式：obj.func()
    属性的调用形式：obj.func
'''

class Foo:
    @property
    def foo1(self):
        print('这是属性')

    @foo1.setter
    def foo1(self,values):
        print('伪装赋值',values)

    @foo1.deleter
    def foo1(self):
        print('伪装删除')
    #上面两个 foo1 都是在装饰第一个 foo1

obj = Foo()

#自动执行 @property 装饰的 foo1 方法并获取返回值
print(obj.foo1)
#自动执行 @foo1.setter 装饰的方法，并将'123'赋值给value
obj.foo1 = 'aaa'
#自动执行 @foo1.deleter 修饰的方法
del obj.foo1

