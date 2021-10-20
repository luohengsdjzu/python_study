#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# 第一类显式布尔值
# 2.1条件可以是：比较运算符
age = 18
print(age > 16)

# 2.2条件可以是：True、False
is_beautiful = True
print(is_beautiful)

# 第二类隐式布尔值，所有值都可以当成条件去用
# 其中0、None、空（空字符串、空列表、空字典）代表的布尔值为False，其余都为True
if 10:
    print('hello')

