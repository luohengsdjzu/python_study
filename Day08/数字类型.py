#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# 一、整形
# 1. 定义
# age = 12  # age = int(12)
# 2. 类型转换
# 2.1  将纯数字的字符串转换成int
res = int('100111')
print(res, type(res))

# 2.2
# 2.2.1 10进制转成其他进制
# 10进制转2进制
print(bin(11))

# 10进制转8进制
print(oct(11))

# 10进制转16进制
print(hex(11))

# 2.2.2 其他进制转成10进制
# 2进制转换成10进制
print(int('0b1011', 2))

# 8进制转换成10进制
print(int('0o13', 8))

# 16进制转换为10进制
print(int('0xb', 16))

# 3. 使用，暂无

# 二、 float类型
# 1. 定义
salary = 3.1
print(type(salary))

# 2. 类型转换
res = float("3.1")
print(res, type(res))

# 3. 使用
# int与float没有需要掌握的内置方法
# 他们的使用就是数学运算和比较运算
