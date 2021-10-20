# 一：储备知识
# 1、*args, **kwargs
# def index(x,y):
#     print(x, y)
#
# def wrapper(*args, **kwargs):   # 此处*args是将多余的位置实参变成元组，然后赋值给args，**kwargs是将多余的关键字实参变成字典，然后赋值给kwargs
#     index(*args, **kwargs)  # 此处将args解析为位置参数，将kwargs解析为关键字参数
#
#
# wrapper(111, 222)

# 2、名称空间与作用域：名称空间的“嵌套”关系是在函数定义阶段，即检测语法的时候确定的

# 3、函数对象：
#   可以把函数当做参数传入
#   可以把函数当作返回值返回
# def index():
#     pass
#
# def foo(func):
#     return func
#
# foo(index)

# 4、函数的嵌套定义：
# def outter():
#     def func():
#         return 0
#     return func

# 5、闭包函数
# def outter():
#     x = 111
#     def wrapper():
#         x
#     return wrapper()
#
# f = outter()

# 二：装饰器
"""
1、什么是装饰器
    装饰器指的定义一个函数，该函数是用来为其他函数添加额外的功能

2、为何要用装饰器
    开发封闭原则
        开放：指的是对拓展功能是开放的
        封闭：指的是对修改源代码是封闭的
    装饰器就是在不修改被装饰对象源代码以及调用方式的前提下，为被装饰对象添加新功能
3、如何用

"""
# 需求：在不修改index函数的源代码以及调用方式的前提下为其添加统计运行时间的功能
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' %(x,y))

# 解决方案一：失败
# 问题：没有修改被装饰对象的调用方式，但是修改了源代码
# import time
#
# def index(x,y):
#     start = time.time()
#     time.sleep(3)
#     print('index %s %s' %(x,y))
#     end = time.time()
#     print(end-start)
#
# index(111, 222)


# 解决方案二：
# 问题：没有修改被装饰对象的调用方式，也没有修改其源代码，并且加上了新功能，但是代码冗余
# import time
#
#
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' %(x,y))
#
# start = time.time()
# index(111,222)
# end = time.time()
# print(end-start)
#
# start = time.time()
# index(111,222)
# end = time.time()
# print(end-start)
#
# start = time.time()
# index(111,222)
# end = time.time()
# print(end-start)

# 解决方案三：解决了方案二代码冗余的问题，但带来了一个新问题即函数的调用方式改变了
# import time
#
#
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' %(x,y))
#
# def wrapper():
#     start = time.time()
#     index(111,222)
#     end = time.time()
#     print(end-start)
#
# wrapper()

# 方案三的优化一:将index的参数写活了，有缺陷，只能装饰index函数
# import time
#
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' %(x, y))
#
# def wrapper(*args, **kwargs):
#     start = time.time()
#     index(*args, **kwargs)
#     end = time.time()
#     print(end-start)
#
#
# wrapper(111, 222)

# 方案三的优化二：在优化一的基础上把被装饰对象写活了，原来只能装饰index
# import time
#
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' %(x, y))
#
# def outter(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#     return wrapper
#
# index = outter(index)
# index(x=1,y=2)

# 方案三的优化三：将wrapper做的跟装饰对象一模一样，以假乱真
# import time
#
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' %(x, y))
#     return 3
#
# def outter(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         x = func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#         return x
#     return wrapper
#
# index = outter(index)
# res = index(x=1,y=2)
# print("返回值->",res)


# 大方向：如何在方案三的基础上不改变函数的调用方式

# 语法糖：
# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         x = func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#         return x
#     return wrapper
#
#
# @timer      # 相当于timer = timer(index)
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' %(x, y))
#     return 3
#
#
# @timer      # 相当于timer = timer(home)
# def home(name):
#     time.sleep(2)
#     print('welcome %s' %(name))
#     return 123
#
#
# res = index(x=1,y=2)
# print("返回值->",res)
# res = home('egon')
# print('返回值是-》',res)

# 总结无参装饰器模板
def outter(func):
    def wrapper(*args, **kwargs):
        # 1、调用原函数
        # 2、为其增加新功能
        res = func(*args, **kwargs)
        return res
    return wrapper


