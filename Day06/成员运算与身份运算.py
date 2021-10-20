#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# 1、成员运算符
print('hello' in 'hello world')
print(111 in [111, 222, 333])
print(111 in {'k1': 111, 'k2': 222})
print('k1' in {'k1': 111, 'k2': 222})  # 对于字典in操作判断的是key

# not in
print('hello' not in 'hello world')
print(not 'hello' in 'hello world')

# 2、身份运算
# is    判断id是否相等

