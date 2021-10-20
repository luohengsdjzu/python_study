#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# 元组就是一个”不可变的列表“
# 1、作用：按照索引/位置存放多个值，只用于读不用于改
# 2、定义：()内用逗号分割开多个任意类型的元素
t = (1, 1.3, 'aaa')     # t = tuple((1, 1.3, 'aaa'))
print(t, type(t))

x = (10)
print(x, type(x))

x = (10,)
print(x, type(x))

x = 10,
print(x, type(x))

t = (1, 1.3, 'aaa')
t[0] = 1111

t = (1, [11, 22])
print(id(t[0]), id(t[1]))
t[1][0] = 11111
print(t)
print(id(t[0]), id(t[1]))

# 3、类型转换
print(tuple('hello'))
print(tuple([1, 2, 3]))
print(tuple({'a1':111, 'a2':222}))


# 4、内置方法
# 优先掌握的操作
# 1.按索引取值（正向取+反向取）：只能取
t = ('aaa', 'bbb', 'ccc')
print(t[0])
print(t[-1])

# 2.切片（顾头不顾尾，步长）
t = ('aaa', 'bbb', 'ccc', 'ddd')
print(t[0:3])
print(t[::-1])

# 3.长度
t = ('aaa', 'bbb', 'ccc', 'ddd')
print(len(t))

# 4.成员运算in和not in
print('aaa' in ('aaa', 'bbb', 'ccc', 'ddd'))

# 5.循环
t = ('aaa', 'bbb', 'ccc', 'ddd')
for x in t:
    print(x)

# 6.
t = (2, 3, 111, 111, 111, 111)
print(t.index(111))
# print(t.index(1111111))     # 报ValueError异常
print(t.count(111))
