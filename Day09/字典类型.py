#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# 1、作用

# 2、定义：在{}内用逗号分割开多个key:value，其中value可以是任意类型，但是key必须是不可变类型
d = {'k1': 111, (1, 2, 3): 222}
print(d['k1'])
print(d[(1, 2, 3)])
print(type(d))
d = {}      # 默认定义出来的是空字典，而不是空集合
print(d, type(d))
d = dict(x=1, y=2, z=3)
print(d)

# 3、数据类型转换
info = [
    ['name', 'egon'],
    ['age', 18],
    ['gender', 'male']
]

# d = {}
# for k,v in info:
#     d[k] = v
# print(d)
res = dict(info)
print(res)

# 造字典的方式:快速初始化字典
keys = ['name', 'age', 'gender']
# d = {}
# for k in keys:
#     d[k] = None
# print(d)
d = {}.fromkeys(keys,None)
print(d)



# 4、内置方法
# 优先掌握的操作
# 1.按key存取值：可存可取
d = {'k1': 111}
# 针对赋值操作，key存在则修改
d['k1'] = 222
# 针对赋值操作，key不存在则创建新值
d['k2'] = 333
print(d)

# 2.长度len
d = {'k1': 111, 'k2':222, 'k1':333, 'k1':444}
print(d)
print(len(d))

# 3.成员运算in和not in
d = {'k1':111, 'k2':222}
print('k1' in d)
print(111 in d)

# 4.删除
d = {'k1': 111, 'k2': 222}
# 通用删除方法
del d['k1']
print(d)
# 4.1pop()删除:根据key删除元素，返回删除key对应的那个value值
d = {'k1': 111, 'k2': 222}
res = d.pop('k2')
print(d)
print(res)
# 4.2popitem():随机删除，返回元组(k,v)
d = {'k1': 111, 'k2': 222, 'k3':333}
res = d.popitem()
print(d)
print(res)
# 5.键keys()，值values()，键值对items()  ==>在python3中得到的是老母鸡
'''
在python2中返回的是列表
>>> d = {'k1': 111, 'k2': 222}
>>> d.keys()
['k2', 'k1']
>>> d.values()
[222, 111]
>>> d.items()
[('k2', 222), ('k1', 111)]
'''

# 6.for循环
d = {'k1': 111, 'k2': 222, 'k3':333}
for k in d.keys():
    print(k)
for k in d:
    print(k)
for v in d.values():
    print(v)
for k,v in d.items():
    print(k,v)

# 需要掌握的内置方法
# 1. d.clear()：清空字典
d = {'k1':111}
d.clear()
print(d)

# 2. d.update()：用新字典更新老字典，老字典没有的就添加，老字典有的就更新
d = {'k1':111}
d.update({'k2':222,'k3':333,'k1':1111111})
print(d)

# 3. d.get():根据key取值，容错性更好
d = {'k1': 111}
# print(d['k2'])      # key不存在会报错
print(d.get('k1'))
print(d.get('k2'))          # key不存在返回None

# 4. d.setdefault():如果key有则不添加，如果key没有则添加
d = {'k1':111}
res=d.setdefault('k1')
print(res)
res=d.setdefault('k2')
print(res)
print(d)

