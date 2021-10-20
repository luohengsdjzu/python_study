#!/usr/bin/env python
# -*- encoding:utf-8 -*-


"""
1、什么是for循环
    循环就是重复做某件事，for循环是python提供第二种循环机制
2、为何要有for循环
    理论上for循环能做的事情，while循环都可以做
    之所以要有for循环，是因为for循环在循环取值（遍历取值）比while循环更简洁
3、如何用for循环
    语法：
    for 变量名 in 可迭代对象:   # 可迭代对象可以是:列表、字典、字符串、元组、集合
        代码1
        代码2
        代码3
"""

# 一、for循环基本使用
# 1、循环取值
# 简单版
# l = ['zhang', 'yang', 'luo']
# for x in l:
#     print(x)

# 复杂版
# l = ['zhang', 'yang', 'luo']
# i = 0
# while i < 3:
#     print(l[i])
#     i += 1

# 2、字典循环取值
# 简单版
# dic = {'k1':111, 'k2':222, 'k3':333}
# for k in dic:
#     print(k, dic[k])
# 复杂版：while循环可以遍历字典，太麻烦了

# 3、字符串循环取值
# 简单版
# msg = "hello,world"
# for ch in msg:
#     print(ch)

# 二、总结for循环与while循环的异同
# 1、相同之处：都是循环，for循环可以干的事，while循环也可以干
# 2、不同之处：
#           while循环称之为条件循环，循环次数取决于条件何时变为False
#           for循环称之为“取值循环”，循环次数取决于in后包含的值的个数

# 三、for+range
# for i in range(3):
#     print("===>")

# user_name = 'egon'
# user_password = 123
# for i in range(3):
#     inp_name = input("请输入你的账号：")
#     inp_pwd = input("请输入你的密码：")
#
#     if inp_name == user_name and inp_pwd == user_password:
#         print("登录成功")
#         break
# else:
#     print("密码错误次数超过三次")

# 四、range补充
# 1、for搭配range可以按照索引取值，但是麻烦，所以不推荐
# l = ['aaa', 'bbb', 'ccc']
# for i in range(len(l)):
#     print(i, l[i])
#
# for i in l:
#     print(i)
# 2、range()在python3中得到的是一只”会下蛋的老母鸡“

# 五、for+continue
# for i in range(6):
#     if i == 4:
#         continue
#     print(i)
# 六、for循环嵌套:外层循环循环一次，内层循环需要完整地循环完毕
# for i in range(3):
#     print("外层循环-->", i)
#     for j in range(5):
#         print("内层循环", j)
# 终止for循环只有break一种方案
# print补充
print('hello', 'world', 'egon')
print("hello", end='')
print('world')
print('hello',end='8')


