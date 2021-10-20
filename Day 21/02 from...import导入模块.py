# import导入模块在使用时必须加前缀“模块.”
# 优点：肯定不会与当前名称空间中的名字冲突
# 缺点：加前缀麻烦


# from ... import ...导入也发生了三件事
# 1、产生一个模块的名称空间
# 2、运行foo.py将运行过程中产生的名字都丢到模块的名称空间去
# 3、在当前名称空间中拿到一个名字，该名字指向模块名称空间中的某一个内存地址
# from foo import x
# from foo import get
# from foo import change


# print(x)
# print(get)
# print(change)


# get()
# change()
# get()
# print(x)            # x还是指向原来的地址

# 要想改变x的值怎么办，重新导入x
# from foo import x
# print(x)

# from ... import ...导入模块在使用时不用加前缀
# 优点：代码更精简
# 缺点：容易与当前名称空间混淆

# 一行导入多个名字（不推荐）
# from foo import x,get,change

# *：导入模块中所有名字
# from foo import *
# print(x)
# print(get)
# print(change)

# from foo import *
# print(x)
# print(get)
# print(change)

# 起别名
from foo import get as g
print(g)
