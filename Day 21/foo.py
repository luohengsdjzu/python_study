print('模块foo=====>')

x = 1

def get():
    print(x)

def change():
    global x
    x = 0

__all__=['x', ]    # 控制导入的内容
# print(__name__)
# 1、当foo.py被运行时，__name__的值为__main__
# 2、当foo.py被当做模块导入时，__name__的值为foo
# if __name__ == '__main__':
#     print('文件被执行')
#     get()
#     change()
# else:
#     print('文件被导入')
#     pass

if __name__ == '__main__':
    get()

