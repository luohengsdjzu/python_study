# 题目一
input = 333
def func():
    input = 444


func()
print(input)        # 333


# 题目二
def func():
    print(x)
x=111
func()  # 111

# 题目三
x = 1
def func():
    print(x)
def foo():
    x = 222
    func()
# x = 333
foo()       # 1

# 题目四
input = 111
def f1():
    def f2():
        # input = 333
        print(input)
    input = 222
    f2()
f1()        # 222
