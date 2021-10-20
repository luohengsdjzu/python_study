# 偷梁换柱，即将原函数名指向的内存地址偷梁换柱成wrapper函数
import time
from functools import wraps

def outter(func):
    @wraps(func)    # 把func的属性赋值给wrapper
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
        # 将原函数的属性赋值给wrapper函数
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
    return wrapper


@outter
def index(x, y):
    '''打印x和y'''
    time.sleep(2)
    print("%s %s" %(x, y))


index(119, 334)

print(index.__name__)
print(index.__doc__)
print(index.__annotations__)

'''
今日内容：
    有参装饰器（需要掌握）

    迭代器
        for循环的工作原理

    生成器：yield

    三元表达式

    生成式
        列表生成式
        字典生成式
        生成器表达式
    
'''