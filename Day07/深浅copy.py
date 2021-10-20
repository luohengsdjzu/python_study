#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# 浅copy：把原列表第一层内存地址不加区分完全拷贝一份给新列表
# 对不可变类型没有任何问题，对可变类型的话，两个列表就粘到一起了
# list1 = ['egon', 'lxx', [1, 2]]
# list3 = list1.copy()
# print(list1)
# print(list3)
# list1[0] = 'EGON'
# list1[1] = 'LXX'
# list1[2][0] = 111
# list1[2][1] = 222
# print(list1)
# print(list3)

# 深copy：对可变类型和不可变类型加以区分，对于不可变类型直接拷贝内存地址
# 对于可变类型，直接产生一个新的内存地址

import copy
list1 = ['egon', 'lxx', [1, 2]]
list3 = copy.deepcopy(list1)
print(id(list1))
print(id(list3))
print(id(list1[0]), id(list1[1]), id(list1[2]))
print(id(list3[0]), id(list3[1]), id(list3[2]))

list1[0] = 'EGON'
list1[1] = 'LXX'
list1[2][0] = 111
list1[2][1] = 222
print(list1)
print(list3)
