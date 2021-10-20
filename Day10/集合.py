#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# 1.作用
# 1.1 关系运算
friends1 = ['zero', 'kevin', 'jason', 'egon']
friends2 = ['jy', 'ricky', 'jason', 'egon']
l = []
for x in friends1:
    if x in friends2:
        l.append(x)
print(l)
# 1.2 去重


# 2. 定义：在{}内用逗号分割开多个元素，多个元素满足以下三个条件：
#              1.集合内元素必须为不可变类型
#              2.集合内元素无序
#              3.集合内元素没有重复

s = {1,2}
print(s, type(s))

# s = {1, [1, 2]} # TypeError集合内元素必须为不可变类型
s = {1, 'a', 'z', 'b', 4, 7}    # 集合内元素无序
s = {1, 1, 1, 1, 1, 1, 'a', 'b'}    # 集合内元素没有重复
print(s)

# 了解
s = {}
print(type(s))
s = set()
print(type(s))

# 3. 类型转换
# set({1, 2, 3})
res = set('hellollll')
print(res)

print(set([1, 1, 1, 1, 1]))
# print(set([1, 1, 1, 1, 1, [111,222]]))      # 集合的元素必须是不可变类型
print(set({'k1':1, 'k2':2}))

# 4. 内置方法
# 关系运算符
# 4.1 取交集，两者共同的好友
friends1 = {'zero', 'kevin', 'jason', 'egon'}
friends2 = {'jy', 'ricky', 'jason', 'egon'}
res = friends1 & friends2
print(res)
print(friends1.intersection(friends2))

# 4.2 取合集：两者所有的好友
print(friends1 | friends2)
print(friends1.union(friends2))
# 4.3 取差集：取friends1独有的好友
print(friends1-friends2)
print(friends1.difference(friends2))
# 取friends2独有的好友
# print(friends2-friends1)
# 4.4 对称差集：求两个用户独有的好友们
print(friends1 ^ friends2)
print(friends1.symmetric_difference(friends2))
# 4.5 父子集：包含的关系
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1 > s2)
print(s1.issuperset(s2))
print(s2.issubset(s1))

# 去重
# 1. 只能针对不可变类型去重
print(set([1, 1, 1, 1, 2]))

# 2. 无法保证原来的顺序
l = [1, 'a', 'b', 'z', 1, 1, 1, 2]
l = list(set(l))
print(l)

l = [
    {'name':'lili', 'age':18, 'sex':'male'},
    {'name':'jack', 'age':73, 'sex':'male'},
    {'name':'tom', 'age':20, 'sex':'female'},
    {'name':'lili', 'age':18, 'sex':'male'},
    {'name':'lili', 'age':18, 'sex':'male'},
]
new_l = []
for dic in l:
    if dic not in new_l:
        new_l.append(dic)
print(new_l)

# 集合的其他操作
# 1. 长度
s = {'a', 'b', 'c'}
print(len(s))
# 2. 成员运算
print('c' in s)
# 3. 循环
for item in s:
    print(item)

# 其他内置方法
# s.discard() 需要掌握
s = {1, 2, 3}
s.discard(1)
s.discard(123)
print(s)

# s.remove()如果成员不存在，产生keyError
s = {1, 2, 3}
# s.remove(4)   抛出异常

# s.update()需要掌握
s.update({1, 3, 5})     # 两个集合求并集
print(s)

# s.difference_update()

s = {1, 2, 3}
s.difference_update({3,4,5})
print(s)

# s.pop() 需要掌握
s = {1, 2, 3}
res = s.pop()
print(s)
print(res)

# s.add() 需要掌握
s = {1, 2, 3}
s.add(4)
print(s)

# s.isdisjoint() 如果两个集合没有交集，返回True
s = {1, 2, 3}
print(s.isdisjoint({6, 7}))

