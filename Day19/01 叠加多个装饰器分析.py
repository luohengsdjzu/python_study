# 一、叠加多个装饰器的加载，运行分析

def deco1(func):
    def wrapper1(*args, **kwargs):
        print('正在运行===>deco1.wrapper1')
        res1 = func(*args, **kwargs)
        return res1

    return wrapper1


def deco2(func):
    def wrapper2(*args, **kwargs):
        print('正在运行===>deco2.wrapper2')
        res2 = func(*args, **kwargs)
        return res2

    return wrapper2


def deco3(x):
    def outter3(func):
        def wrapper3(*args, **kwargs):
            print('正在运行===>deco3.wrapper3')
            res3 = func(*args, **kwargs)
            return res3

        return wrapper3

    return outter3


# 加载顺序自下而上（了解）
@deco1          # func->wrapper2, @deco1装时候返回wrapper1，最后index->wrapper1
@deco2          # func->wrapper3，@deco2装饰后返回wrapper2,最后index->wrapper2
@deco3(111)     # @deco3(111)相当于@outter3,@outter3装饰后返回wrapper3，最后index->wrapper3
def index(x, y):
    print('from index %s %s' % (x, y))


print(index)
# 运行顺序自上而下
index(5, 6)


