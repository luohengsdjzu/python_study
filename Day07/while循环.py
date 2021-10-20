#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# 1、while循环基本使用
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# print('顶级代码======')


# 2、死循环与效率问题
# count = 0       # 程序会陷入死循环
# while count < 5:
#     print(count)

# while True:
#     name = input('your name:')
#     print(name)
# 纯计算无IO的死循环会导致致命的效率问题
# while True:
#     1+1

# 3、循环的应用
# username = 'egon'
# password = '123'
# while True:
#     inp_name = input('请输入您的账号：')
#     inp_pwd = input('请输入您的密码：')
#     if inp_name == username  and inp_pwd == password:
#         print('登录成功')
#     else:
#         print('登录失败')


# 4、退出循环的两种方式
# 方式一:将条件改为False，等到下次循环判断条件时才会生效
# username = 'egon'
# password = '123'
# tag = True
# while tag:
#     tag = False
#     inp_name = input('请输入您的账号：')
#     inp_pwd = input('请输入您的密码：')
#     if inp_name == username  and inp_pwd == password:
#         print('登录成功')
#     else:
#         print('登录失败')

# 方式二：break，只要运行到break就会立刻终止本层循环

# username = 'egon'
# password = '123'
# while True:
#     inp_name = input('请输入您的账号：')
#     inp_pwd = input('请输入您的密码：')
#     if inp_name == username  and inp_pwd == password:
#         print('登录成功')
#         break           # 立刻终止本层循环
#     else:
#         print('登录失败')
#     print("====end====")

# 5、循环的嵌套
# 每一层都必须配一个break
'''
while True:
    while True:
        while True:
            break
        break
    break
'''

# username = 'egon'
# password = '123'
# while True:
#     inp_name = input('请输入您的账号：')
#     inp_pwd = input('请输入您的密码：')
#     if inp_name == username  and inp_pwd == password:
#         print('登录成功')
#         while True:
#             cmd = input("请输入命令：")
#             if cmd == 'q':
#                 break
#             print('命令{x}正在执行'.format(x=cmd))
#         break           # 立刻终止本层循环
#     else:
#         print('登录失败')
#     print("====end====")

# 6、while+continue结束本次循环
# count = 0
# while count < 6:
#     if count == 4:
#         count += 1
#         continue
#     else:
#         print(count)
#     count += 1

# 7、while+else小案例
# count = 0
# while count < 6:
#     if count == 4:
#         count += 1
#         continue
#     print(count)
#     count += 1
# else:
#     print('else包含的代码会在while循环结束后，并且while循环是在没有被break打断的情况下正常结束的，才会运行')



# count = 0
# while count < 6:
#     if count == 4:
#         break
#     print(count)
#     count += 1
# else:
#     print('====>')


username = 'egon'
password = '123'
count = 0
while count < 3:
    inp_name = input('请输入您的账号：')
    inp_pwd = input('请输入您的密码：')
    if inp_name == username  and inp_pwd == password:
        print('登录成功')
        while True:
            cmd = input("请输入命令：")
            if cmd == 'q':
                break
            print('命令{x}正在执行'.format(x=cmd))
        break           # 立刻终止本层循环
    else:
        print('登录失败')
        count += 1
else:
    print('失败三次，账号锁定30s')
