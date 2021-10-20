#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# 指针移动的单位是以byte/字节为单位
# 只有一种特殊情况：
#       t模式下的read(n),n代表的是字符个数

# with open('aaa.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read(4)
#     print(res)

# f.seek(n,模式)  n指定移动字节数
# 模式：
# 模式0：参照物是文件开头位置
# f.seek(9,0)   # 9
# f.seek(3,0)   # 3

# 模式1：参照物是当前指针所在位置
# f.seek(9, 1)
# f.seek(3, 1)  # 12

# 模式2：参照物是文件末尾位置，应该倒着移动
# f.seek(-9, 2)   # 3
# f.seek(-3, 2)   # 9

# f.tell()  # 获取文件指针当前位置

# 强调：只有0模式可以在t下使用，1、2必须在b模式下用

# 示范
with open(r'aaa.txt', mode='rb') as f:
    f.seek(-9, 2)
    f.seek(-3, 2)
    print(f.tell())
    # f.seek(4, 0)
    # res = f.read()
    # print(res.decode('utf-8'))
    print(f.read().decode('utf-8'))

