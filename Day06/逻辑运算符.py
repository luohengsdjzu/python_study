#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# 一、not and or 的基本使用
# not：把紧跟其后的条件结果取反
# not与紧跟其后的那个条件是一个不可分割的整体
print(not 16 > 13)
print(not True)
print(not False)
print(not 10)
print(not 0)
print(not None)
print(not '')

# and: 逻辑与，and用来连接左右两个条件，两个条件同时为True，最终结果才为True
print(True and 10 > 3)
print(True and 10 > 3 and 10 and 0)

# or: 逻辑或，or用来连接左右两个条件，两个条件但凡有一个为True，最终结果就为True
print(3 > 2 or 0)
print(10 or 3 != 2 or 3 > 2 or True)
print(3 > 2 or 3 != 2 or 3 > 2 or True)

# 二、not and or 的优先级：not > and > or
res = 3 > 4 and not 4 > 3 or 1 == 3 and 'x' == 'x' or 3 > 3
print(res)
