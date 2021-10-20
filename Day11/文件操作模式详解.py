#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# 以t模式为基础进行内容操作
# 1、r（默认的操作模式）：只读模式，当文件不存在时报错，当文件存在时文件指针跳到开始位置
# with open('c.txt', mode='rt', encoding='utf-8') as f:
#     print('第一次读'.center(50, '*'))
#     res = f.read()      # 把所有内容从硬盘读入内存
#     print(res)
#
#     print('第二次读'.center(50, '*'))
#     res1 = f.read()     # 第二次读为空，因为文件指针已经移动到文件末尾
#     print(res1)

# ==========案例========
# inp_user = input('your name:')
# inp_passwd = input('your passwd:')
# with open('user.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         user, passwd = line.strip('\n').split(':')
#         if inp_user == user and inp_passwd == passwd:
#             print('登录成功')
#             break
#     else:
#         print('登录失败')

# 2、w:只写模式，当文件不存在时会创建空文件，当文件存在时会清空文件，指针位于开始位置
# with open('d.txt', mode='wt', encoding='utf-8') as f:
#     # f.read()    # 不可读
#     f.write('哈哈哈哈哈\n')

# with open('a.txt', mode='rt', encoding='utf-8') as f:
#     f.write('aaa')  # 不可写


# 强调1：
# 在以w模式打开文件没有关闭的情况下，连续写入，新的内容总是跟在旧的之后
# with open('d.txt', mode='wt', encoding='utf-8') as f:
#     # f.read()    # 不可读
#     f.write('哈哈哈哈哈\n')
#     f.write('呵呵呵呵')
# 强调2：
# 如果重新以w模式打开文件，则会清空文件内容
# with open('d.txt', mode='wt', encoding='utf-8') as f:
#     f.write('哈哈哈哈哈\n')
# with open('d.txt', mode='wt', encoding='utf-8') as f:
#     f.write('呵呵呵呵呵\n')

# 案例：w模式用来创建全新的文件
# 复制文件
with open('e.txt', mode='rt', encoding='utf-8') as f1, \
    open('f.txt', mode='wt', encoding='utf-8') as f2:
    res = f1.read()
    f2.write(res)



# 3、a：只追加写，在文档不存在时会创建空文档，在文件存在时文件指针会直接跳到文件末尾
with open('e.txt', mode='at', encoding='utf-8') as f:
    # f.read()        # 报错：not readable
    f.write('哈哈\n')
# 强调 w 模式与 a 模式的异同：
# 1 相同点：在打开文件不关闭的情况下，连续的写入，新写的内容总会跟在之前写的内容之后
# 2 不同点：以a模式重新打开文件、不会清空原文件内容，会将文件指针直接移动到文件末尾

# 案例
# 注册功能
name = input('your name>>:')
pwd = input('your pwd>>:')
with open('db.txt', mode='at', encoding='utf-8') as f:
    f.write('{}:{}\n'.format(name, pwd))

# 了解：+不能单独使用，必须配合r、w、a
with open('g.txt', mode='r+', encoding='utf-8') as f:
    # print(f.read())
    f.write('你是谁')

with open('g.txt', mode='w+', encoding='utf-8') as f:
    f.write('111\n')
    f.write('222\n')
    f.write('333\n')
    print('=====>',f.read())

with open('g.txt', mode='a+', encoding='utf-8') as f:
    f.write('444\n')
    f.write('555\n')
    f.read()
