#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# 1、作用：按位置存放多个值

# 2、定义
# l = [1, 1.2, 'a']

# 3、类型转换
# 但凡能够被for循环遍历的类型都可以当做参数传给list()转成列表
res = list('hello')
print(res)

res = list({'k1': 111, 'k2': 222, 'k3': 333})   # 字典是无序的
print(res)  # 字典循环的是key

# 4、内置方法
# 优先掌握的操作
# 1.按索引存取值（正向存取+反向存取）：既可以取，也可以改
l = [111, 'egon', 'hello']
# 正向取
print(l[0])
# 反向取
print(l[-1])
# 可以取也可以改：索引存在就修改值，不存在就抛出异常
l[0] = 222
print(l)

# 2.切片（顾头不顾尾，步长）
l = [111, 'egon', 'hello', 'a', 'b', 'c', 'd', [1, 2, 3]]
print(l[0:5:2])
print(l[:])     # 切片等同于拷贝行为，而且相当于浅copy
new_l = l[:]
print(id(l))
print(id(new_l))
l[-1][0] = 111
print(l)
print(new_l)

print(l[::-1])  # 列表逆序

# 3.长度
print(len([1, 2, 3]))

# 4.成员运算in和not in
print('aaa' in ['aaa', 1, 2])
print(1 in ['aaa', 1, 2])
# 5.往列表里面添加值
# 5.1追加
l = [111, 'egon', 'hello']
l.append(333)
l.append(444)
print(l)
# 5.2插入
l = [111, 'egon', 'hello']
l.insert(1, 'alex')
print(l)
# 5.3 extend
new_l = [1, 2, 3]
l = [111, 'egon', 'hello']
l.extend(new_l)
print(l)
l.extend('abc')
print(l)

# 7.删除
# 方式一：通用的删除方法，只是单纯的删除、没有返回值
l = [111, 'egon', 'hello']
del l[1]
print(l)

# 方式二：l.pop()根据索引删除，会返回删除的值
l = [111, 'egon', 'hello']
res = l.pop(1)
print(l)
print(res)

# 方式三：l.remove()根据元素删除，返回值为None
l = [111, 'egon', [1, 2, 3], 'hello']
l.remove([1, 2, 3])
print(l)

res = l.remove('egon')
print(res)


# 8.循环
for x in [1, 'aaa', 'bbb']:
    print(x)


# 需要掌握的操作
l = [1, 'aaa', 'bbb', 'aaa', 'aaa']
# 1. l.count()
print(l.count('aaa'))
# 2. l.index()
print(l.index('aaa'))
# print(l.index('aaaaaa'))        # 找不到的话会报错
# 3. l.clear()
l.clear()
print(l)
# 4. l.reverse()：不是排序，就是将列表倒过来
l = [1, 'egon', 'alex', 'lxx']
l.reverse()
print(l)        # 修改的是原列表
# 5. l.sort()：列表内元素必须是同种类型才可以排序
l = [11, -3, 9, 2]
l.sort()        # 默认升序排列
print(l)
l.sort(reverse=True)
print(l)

l = ['c', 'e', 'a'] # 字符串比较大小，是按照ASCII码表顺序比较大小
l.sort()
print(l)

# 列表也可以比大小，原理同字符串一样,对应位置的元素必须是同种类型
l1 = [1, 'abc', 'zaa']
l2 = [10, ]
print(l1 < l2)





