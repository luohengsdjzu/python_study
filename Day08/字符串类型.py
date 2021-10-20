#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# 1. 定义
# msg = 'hello'
# print(type(msg))

# 2. 类型转换
# str可以把任意其他类型转换成字符串
# res = str({'a': 1})
# print(res, type(res))
# 3. 使用：内置方法
# 3.1 按索引取值
# msg = 'hello world'
# # 正向取值
# print(msg[0])
# print(msg[5])
# # 反向取值
# print(msg[-1])
# # 只能取值
# msg[0] = 'H'
# 3.2 切片:索引的拓展应用，从一个字符串中拷贝出一个子字符串
# msg = 'hello world'
# print(msg[0:5])
# print(msg)
# # 指定步长切片
# print(msg[0:5:2])
# # 反向步长
# print(msg[5:0:-1])
# msg = 'hello world'
# res = msg[:]    # res = msg[0:11]
# print(res)
#
# res = msg[::-1]     # 把字符串倒过来
# print(res)

# 3.3 长度
# msg = 'hello world'
# print(len(msg))

# 3.4 成员运算in和not in
# 判断一个子字符串是否存在于一个大字符串中
# print("alex" in "alex is li")
# print("alex" not in "alex is li")

# 3.5 移除字符串左右两侧的符号strip
# msg = '   egon    '
# res = msg.strip()         # 默认去掉的是空格
# print(msg)          # 不会改变原值
# print(res)          # 产生新的值
#
# msg = '***egon**'
# print(msg.strip('*'))

# # strip只去掉两边，不会去掉中间的符号
# msg = '***eg**on****'
# print(msg.strip('*'))
# msg = '-=-=---==egon(***'
# print(msg.strip('-=(*'))

# 3.6 切分split: 把一个字符串按照某种分隔符进行切分，得到一个列表
# 默认分隔符是空格
# info = 'egon 18 male'
# res = info.split()
# print(res)


# # 指定分隔符
# info = 'egon:18:male'
# res = info.split(':')
# print(res)
#
# # 指定分割次数
# info = 'egon:18:male'
# res = info.split(':', 1)
# print(res)

# 3.7循环
# info = 'hello'
# for x in info:
#     print(x)

# 需要掌握的操作
# 4.1 strip lstrip rstrip
msg = '***egon***'
print(msg.strip('*'))
print(msg.lstrip('*'))
print(msg.rstrip('*'))

# 4.2 lower upper
msg = 'AbbbCCC'
print(msg.lower())
print(msg.upper())

# 4.3 startswith, endswith
print('zhang xin'.startswith('zhang'))
print('zhang xin'.endswith('in'))

# 4.4 split, rsplit: 将字符串切成列表
info = 'egon:18:male'
print(info.split(':', 1))
print(info.rsplit(':', 1))

# 4.5 join：把列表拼接成字符串
l = ['egon', '18', 'male']
res = ':'.join(l)
print(res)

# 4.6 replace:替换
msg = "hello, wei, hello"
print(msg.replace('hello', 'hi', 1))

# 4.7 isdigit:判断字符串是否由数字组成
print('123'.isdigit())
print('1.23'.isdigit())

# age = input("your age:")
# if age.isdigit():
#     print('you age is {}'.format(age))
# else:
#     print("必须输入数字")

# 了解
# 1. find,rfind,index,rindex,count
msg = 'hello egon haha'
print(msg.find('e'))  # 返回要查找的字符串在大字符串中的起始位置
print(msg.find('egon'))  # 返回要查找的字符串在大字符串中的起始位置
print(msg.index('e'))
print(msg.index('egon'))
# index和find的区别在于找不到子串的时候，find返回-1，index会抛出异常
print(msg.find('xxx'))
# print(msg.index('xxx'))   # 会抛出异常

msg = 'hello egon,hi egon egon'
print(msg.count('egon'))

# 2. center ljust rjust zfill
print('egon'.center(50, 'x'))       # egon居中显示，不够的用‘x’填充
print('egon'.ljust(50, '*'))
print('egon'.rjust(50, '*'))
print('egon'.zfill(10))

# 3. expandtabs
msg = 'hello\tworld'
print(msg.expandtabs(2))        # 设置制表符代表的空格数为2

# 4. captalize swapcase title
print('hello world'.capitalize())
print('hello world'.swapcase())
print('hello world'.title())

# 5. is
print('abc'.islower())
print('ABC'.isupper())
print('Hello World'.istitle())
print('123abc'.isalnum())   # 字母或数字组成
print('abc'.isalpha())      # 字母组成
print('   '.isspace())
print('luo'.isidentifier())     # 判断变量是否合法
