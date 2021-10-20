# -*- encoding:utf-8 -*-

# 垃圾回收机制详解
# 1、引用计数
# x = 10  # 直接引用
# print(id(x))
#
# l = ['a', x]  # 间接引用
# print(id(l[1]))
#
# d = {'name': x}     # 间接引用
# print(id(d['name']))

x = 10
l = ['a', 'b', x]   # 列表当中实际上存的是内存地址，跟x变量没关系

x = 123
print(l[2])
print(x)


# 2、标记清除
# 3、分代回收
