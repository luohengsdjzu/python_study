# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
# 会返回一个生成器对象，生成器即自定义的迭代器

# def func():
#     print('第一次')
#     yield 1
#     print('第二次')
#     yield 2
#     print('第三次')
#     yield 3
#     print('第四次')
#
# g = func()  # 返回一个生成器对象
# # print(g)
# # g.__iter__()
# # g.__next__()
#
# # 会触发函数体代码的运行，然后遇到yield停下来，将yield后的值
# # 当做本次调用的结果返回
#
# res1 = next(g)
# print(res1)
#
# res2 = next(g)
# print(res2)
#
# res3 = next(g)
# print(res3)
#
# # res4 = g.__next__()     # 抛出异常StopIteration
#
# # print('aaa'.__len__())
# # print(len('aaa'))


# 应用案例：
# range(1, 1000)在python3中是可迭代对象

def my_range(start, end, step=1):
    while start<end:
        yield start
        start += step


g = my_range(1, 1000000000000000)
print(g)
print(iter(g))
for i in my_range(1, 10):
    print(i)

