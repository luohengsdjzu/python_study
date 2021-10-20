# 1、def用于定义有名函数
# func=函数的内存地址
# def func(x,y):
#     return x+y
#
#
# print(func)
# 2、lambda用于定义匿名函数
# print(lambda x,y:x+y)


# 3、调用匿名函数
# 方式一:
# print((lambda x,y:x+y)(1,2))

# 方式二：
# func = lambda x,y:x+y
# res = func(1,2)
# print(res)


# 4、匿名函数用于临时调用一次的场景:更多的是将匿名函数与其他函数配合使用
# salaries = {
#     'siry':3000,
#     'tom':7000,
#     'lili':10000,
#     'jack':2000
# }

# 需求：找出薪资最高的人
# def func(k):
#     return salaries[k]
#
# print(max(salaries,key=func))

# print(max(salaries,key=lambda k:salaries[k]))




# sorted排序
# salaries = {
#     'siry':3000,
#     'tom':7000,
#     'lili':10000,
#     'jack':2000
# }
#
# res = sorted(salaries, key=lambda k:salaries[k], reverse=True)
# print(res)
# print(min(salaries, key=lambda k:salaries[k]))


# map应用(了解)
# l = ['alex', 'lxx', 'wxx', 'lll']
# # new_l = [name+'_dsb' for name in l]
# # print(new_l)
#
# res = map(lambda name:name+'_dsb', l)
# print(res)  # 生成器

# # filter应用（了解）filter保留运算结果为True的值
# l = ['alex_sb', 'lxx_sb', 'wxx', 'lll']
# # res = [name for name in l if name.endswith('_sb')]
# # print(res)
#
# res = filter(lambda name:name.endswith('_sb'), l)
# print(res)      # 生成器

# reduce应用
from functools import reduce
res = reduce(lambda x,y:x+y, [1, 2, 3], 10)
print(res)

res = reduce(lambda x,y:x+y, ['a', 'b', 'c'])
print(res)
