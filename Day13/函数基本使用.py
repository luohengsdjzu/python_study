#!/usr/bin/env python
# encoding:utf-8


# 1、先定义
# 定义的语法
'''
def 函数名(参数1,参数2,...):
    """文档描述"""
    函数体
    return 值
'''


# 函数的命名规范和变量名一样，用小写字母加下划线
# 形式一：无参函数
# def func():
#     print('哈哈哈')
#     print('哈哈哈')
#     print('哈哈哈')
#
#
# func()
# 定义函数发生的事情
# 1、申请内存空间保存函数体代码
# 2、将上述内存地址绑定函数名
# 3、定义函数不会执行函数体代码，但是会检测函数体语法

# 调用函数发生的事情
# 1、通过函数名找到函数的内存地址
# 2、然后加括号就是在触发函数体代码的执行
# print(func)

# 示范1
# def bar():
#     print('from bar')
#
#
# def foo():
#     # print(bar)
#     bar()
#     print('from foo')
#
#
# foo()


# 示范2
# def foo():
#     # print(bar)
#     bar()
#     print('from foo')
#
#
# def bar():
#     print('from bar')
#
#
#
# foo()

# 形式二：有参函数
# def func(x, y):
#     print(x, y)
#
# func(4, 5)

# 形式三：空函数，函数体代码为pass
# def func(x, y):
#     pass


# 三种定义方式各用在何处
# 1、无参函数的应用场景
# def interactive():
#     name = input('username>>')
#     age = input('age>>')
#     msg = '姓名：{} 年龄：{}'.format(name, age)
#     print(msg)
#
# interactive()
# 2、有参函数的应用场景
# def add(x, y):      # 参数相当于原材料
#     res = x + y
#     return res      # 返回值相当于产品
# res = add(3, 22)
# print(res)
# 3、空函数的应用场景
# 适用于函数结构构思的时候


# 二、调用函数
# 1、语句的形式：只加括号调用函数
# interactive()
# add(1,2)

# 2、表达式的形式：
# def add(x, y):      # 参数相当于原材料
#     res = x + y
#     return res      # 返回值相当于产品
# # 赋值表达式
# res = add(3, 22)
# print(res)
# # 数学表达式
# res = add(1, 2) * 10
# print(res)

# 3、函数调用可以当做参数
# res = add(add(1, 2), 10)
# print(res)

# 三、函数返回值
# return是函数结束的标志，即函数体代码一旦运行到return会立刻终止函数的运行，
# 并且会将return后的值当做本次运行的结果返回
# 1、返回None：函数体内没有return
#               return
#               return None

def func():
    print(1111)
    while True:
        while True:
            while True:
                return
    print(2222)
    print(3333)

func()



# 2、返回一个值：return 值
def func():
    return 10
    # pass
res = func()
print(res)

# 3、返回多个值：用逗号分割开多个值，会被return返回成元组
def func():
    return 10,'aa',[1,2]

res=func()
print(res, type(res))
