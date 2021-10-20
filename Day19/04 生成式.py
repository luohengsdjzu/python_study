# 1、列表生成式
# l = ['alex_dsb', 'lxx_dsb', 'wxx_dsb', 'xxq_dsb', 'egon']
# new_l = []
#
# for name in l:
#     if name.endswith('dsb'):
#         new_l.append(name)
#
# print(new_l)

# 把所有小写字母变成大写
# new_l = [name.upper() for name in l]
# print(new_l)
# 把所有名字去掉后缀_dsb
# new_l = [name.replace('_dsb','') for name in l ]
# print(new_l)

# 2、字典生成式
# keys = ['name', 'age', 'gender']
#
# dic = {key:None for key in keys}
# print(dic)


# items = [('name', 'egon'), ('age', 18), ('gender', 'male')]
#
# dic = { k:v for k,v in items if k != 'gender'}
# print(dic)

# 3、集合生成式
# keys = ['name', 'age', 'gender']
# set1 = {key for key in keys}
# print(set1, type(set1))


# 4、生成器表达式（没有元组生成式，元组是不可变类型）
# g = (i for i in range(10) if i>3)
# # 强调此刻g内部一个值也没有
# print(g, type(g))
# print(next(g))
# print(next(g))
# print(next(g))


# 5、统计笔记.txt的字数
# 5.1 方式一
# with open('笔记.txt', 'rt', encoding='utf-8') as f:
#     res = 0
#     for line in f:
#         res += len(line)
#     print(res)

# 5.2 方式二（缺点：当文件行数过多时，列表过长）
# with open('笔记.txt', 'rt', encoding='utf-8') as f:
#     print(sum([len(line) for line in f]))


# 5.3 方式三:效率最高
with open('笔记.txt', 'rt', encoding='utf-8') as f:
    print(sum(len(line) for line in f))
