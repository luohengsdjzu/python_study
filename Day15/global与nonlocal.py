# 示范1：
x = 111   # 全局的x

def func():
    x = 222   # 局部的x

func()
print(x)  # 打印的全局的x，仍为111


# 示范2：如果在全局，想要修改全局的名字对应的值（不可变类型），需要用global
x = 111

def func():
    global x
    x = 222


func()
print(x)


# 示范3：
l = [111, 222]
def func():
    l.append(333)

func()
print(l)


# nolocal(了解)：修改函数外层函数包含的名字对应的值（不可变类型）
x = 0
def f1():
    x = 11
    def f2():
        nonlocal x
        x = 22
    f2()
    print('f1内的x',x)
f1()

def f1():
    x = []
    def f2():
        x.append(111)
    f2()
    print('f1内的x',x)
f1()


