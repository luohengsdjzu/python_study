# /usr/bin/python
# encoding:utf-8

# 一、形参与实参
# 形参：在定义函数阶段定义的参数称之为形式参数，简称为形参，相当于变量名
# def func(x, y):     # x=1,y=2
#     print(x, y)

# 实参：在调用函数阶段传入的值称之为实际参数，简称实参，相当于变量值
# func(1, 2)

# 形参与实参的关系：
# 1、在调用阶段，实参（变量值）会绑定给形参（形参）
# 2、这种绑定关系只能在函数体内使用
# 3、实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定关系


# 二、位置参数
# 2.1 位置参数：按照从左到右的顺序依次定义的参数称之为位置参数
# 位置形参：在函数定义阶段，按照从左到右的顺序直接定义的“变量名”
#       特点：必须被串子，多一个不行少一个也不行
# def func(x,y):
#     print(x,y)
# func(1, 2)
# 位置实参：在函数调用阶段，按照从左到右的顺序依次传入的值
#       特点：按照顺序与形参一一对应

# 2.2 关键字参数
# 关键字实参：在函数调用阶段，按照key=value的形式传入的参数
#       特点：指名道姓给某个形参传值，可以完全不参照顺序
# def func(x,y):
#     print(x,y)
#
# func(y=2,x=1)
# func(1, 2)

# 混合使用
# 1、位置实参必须放在关键字实参前
# func(1, y=2)
# func(y=2 ,1)    # 语法错误，位置实参必须放在关键字实参前
# 2、不能对多个参数同时传多个值
# func(1, 2, x=3, y=4)

# 2.3 默认参数
# 默认参数：在定义函数阶段，就已经被赋值的形参，称之为默认参数
#       特点：在定义阶段就已经被赋值，意味着在调用阶段可以不用为其赋值
# def func(x, y=3):
#     print(x,y)
#
# # func(x=1)
# func(1, 4444)

# 位置参数与默认参数混用，强调：
# 1、位置形参必须在默认参数左边
# def func(x,y=2):
#     print(x,y)
#
# func(1)
#
# # def func(x=1,y):    # 语法错误，位置形参必须在默认参数左边
# #     print(x,y)
#
# func(3)

# 2、默认参数的值是在函数定义阶段被赋值的，准确地说被赋予的值是内存地址
# 示范一：
# m = 2
# def func(x, y=m):   # y==>2的内存地址
#     print(x,y)
# m = 333333
# func(1)

# 示范二：
# m = [1111, ]
# def func(x, y=m):   # 将列表m的内存地址赋值给了y
#     print(x,y)
# m.append(333333)
# func(1)

# 3、 虽然默认值可以被指定为任意数据类型，但是不推荐使用可变类型
# 函数最理想的状态：函数的调用只跟函数本身有关系，不受外界代码的影响


# 2.4 可变长度的参数（*与**的用法）
# 可变长度指的是在调用函数时，传入的值（实参）
# 而实参是用来为形参赋值的，所以对应着，针对溢出的实参必须有对应的形参来接收

# 2.4.1 可变长度的位置参数
# I：*形参格式：用来接受溢出的位置实参，溢出的位置实参会被*保存成元组的格式，然后赋值紧跟其后的形参
#       *后跟的可以是任意名字，但是约定俗成应该是args
# def func(x,y,*z):
#     print(x,y,z)
#
# func(1, 2, 3, 4, 5,)
#
# def my_sum(*args):
#     res = 0
#     for item in args:
#         res += item
#     return res
#
# print(my_sum(1, 2, 3, 4, 5, 6, 7, 8))

# II: *可以用在实参中,实参中带*，先将*后的值打散成位置实参
# def func(x,y,z):
#     print(x, y, z)
#
# # func(*[11, 22, 33])
# # func(*[11, 22])
# l = [11, 22, 33]
# func(*l)


# III: 形参与实参中都带*
# def func(x, y, *args):
#     print(x, y, args)
#
# func(1, 2, [3, 4, 5, 6])
# func(1, 2, *[3, 4, 5, 6])


# 2.4.2 可变长度的关键字参数
# I: **形参名：用来接收溢出的关键字实参，**会将溢出的关键字实参保存成字典格式，然后赋值紧跟其后的形参
#           **后跟的可以是任意名字，但是约定俗成应该是kwargs

# def func(x, y, **kwargs):
#     print(x, y, kwargs)
#
# func(1, y=2, a=1, b=2, c=3)

# II: **可以用在实参中（**后跟的只能是字典）,实参中带**，先将**后的值打散成关键字实参
# def func(x, y, z):
#     print(x, y, z)
#
# func(**{'x':1, 'y':2, 'z':3})
# func(*{'x':1, 'y':2,})      # 有错误，缺少z
# func(**{'x':1, 'a':2, 'z':3})   # 有错误，没有参数a

# III：形参与实参中都带*
# def func(x, y, **kwargs):
#     print(x,y,kwargs)
#
# func(**{'y':222,'x':111,'a':333,'b':444})

# 混用*与**
# *args必须在**kwargs之前

# def func(x, **kwargs, *args):   # 报错，*args必须在**kwargs之前
#     pass

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# func(1,2,3,4,5,6,x=1,y=2,z=3)


# 对wrapper函数的传参原封不动地传递给index函数
def index(x, y, z):
    print('index>>> ',x,y,z)

def wrapper(*args, **kwargs):
    index(*args, **kwargs)

wrapper(1,z=5,y=3)

