# 一：大前提
# 闭包函数=名称空间与作用域+函数嵌套+函数对象
#   核心点：名字的查找关系是以函数定义阶段为准

# 二：什么是闭包函数
# “闭”函数指的该函数是内嵌函数
# “包”函数指的该函数包含对外层函数作用域名字的引用（不是对全局作用域）

# 闭包函数之名称空间与作用域+函数嵌套
def f1():
    x = 3333333333
    def f2():
        print(x)
    f2()

# f1()
def bar():
    x = 1211212121212
    f1()

# bar()

def foo():
    x = 333344444
    f1()
foo()

# 闭包函数：函数对象
def f1():
    x = 3333333
    def f2():
        print(x)
    # f2()
    return f2

f = f1()
# x = 444444
# f()

def foo():
    x = 5555
    f()
foo()



# 三：为何要有闭包函数=》闭包函数的应用
# 两种为函数体传参的方式
# 方式一：直接把函数体需要的参数定义成形参
def f2(x):
    print(x)
f2(1)
f2(2)
f2(3)

# 方式二：
def f2(x):
    def f1():
        print(x)
    return f1

f = f2(4)
print(f)
f()

# 传参的方案一：
import requests
def get(url):
    response = requests.get(url)
    print(len(response.text))

get('https://www.baidu.com')
get('https://www.cnblogs.com/lichengmin')
get('https://zhuanlan.zhihu.com')

# 传参的方案二：
import requests
def outter(url):
    def get():
        response = requests.get(url)
        print(response.text)
    return get

baidu = outter('https://www.baidu.com')
baidu()

cnblogs = outter('https://www.cnblogs.com/lichengmin')
cnblogs()

zhihu = outter('https://zhuanlan.zhihu.com')
zhihu()
