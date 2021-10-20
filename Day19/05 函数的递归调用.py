# 一、递归的定义
# 函数的递归调用：是函数嵌套调用的一种特殊形式
# 具体是指：
#       在调用一个函数的过程中又直接或者间接地调用到本身

# # 直接调用到本身
# def f1():
#     print('是我是我还是我')
#     f1()
#
#
# f1()


# # 间接调用本身
# def f1():
#     print('from f1')
#     f2()
#
#
# def f2():
#     print('from f2')
#     f1()
#
#
# f1()

# 一段代码循环运行的方案有两种：
# 方式一：while、for循环
# while True:
#     print(111)
#     print(222)
#     print(333)

# 方式二：递归的本质就是循环
# def f1():
#     print(111)
#     print(222)
#     print(333)
#     f1()
#
#
# f1()

# 二、需要强调的一点是：
# 递归调用不应该无限地调用下去，必须在满足某种条件下结束递归调用
# def func(n):
#     if n>10:
#         return
#     print(n)
#     n += 1
#     func(n)
#
#
# func(1)


# 三、递归的两个阶段
# 回溯：一层一层调用下去
# 递推：满足某种结束条件，结束递归调用，然后一层一层返回

# def age(n):
#     if n == 1:
#         return 18
#     else:
#         return age(n-1) + 10
#
#
# print(age(5))

# 四、递归的应用
l = [1,2,[3, [4, [5, [6, [7, [8, [9,10,11, [12, 13, [14, [15, [16]]]]]]]]]]]]

def f(l):
    for i in l:
        if type(i) is list:
            f(i)
        else:
            print(i)

f(l)

