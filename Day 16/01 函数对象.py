# 精髓：可以把函数当成变量去用
# func=内存地址

def func():
    print('from func')

# 1、可以赋值
# f = func
# print(f, func)
# f()

# 2、可以把函数当做参数传给另一个函数
# def foo(x):         # x=func的内存地址
#     print(x)
#     x()
#
# foo(func)           # foo(func的内存地址)

# 3、可以把函数当做另外一个函数的返回值
# def foo(x):
#     return x
#
# res = foo(func)
# print(res)
# res()

# 4、可以把函数当作容器类型的一个元素
# l = [func, ]
# print(l)
# l[0]()
#
# dic = {'k1':func}
# print(dic)
# dic['k1']()

# 示例
def register():
    print('注册功能')

def login():
    print('登录功能')

def check():
    print('查询余额')

def pay():
    print('支付功能')

def put():
    print('存款功能')

func_dic = {
    '0': ('退出', None,),
    '1': ('注册', register,),
    '2': ('登录', login,),
    '3': ('查询', check,),
    '4': ('支付', pay,),
    '5': ('存款', put,)
}

while True:
    for k in func_dic:
        print(k, func_dic[k][0])
    choice = input('请输入你的选择:')
    if choice == '0':
        break

    if not choice.isdigit():
       print('请输入数字')

    if choice in func_dic:
        func_dic[choice][1]()
    else:
        print('输入数字无效')
