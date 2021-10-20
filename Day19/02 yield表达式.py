# 一：yield先返回值并挂起函数，再接收值继续运行
def dog(name):
    print('dog %s 准备吃东西啦' %name)
    while True:
        # x拿到的是yield接收到的值
        x = yield
        print('dog %s 吃了 %s' %(name, x))


g = dog('alex')         # 包含有yield的函数被调用，返回一个生成器对象
res = g.send(None)            # 相当于next(g)，初始化并使函数挂在yield
print(res)
res = g.send('一根顾头')
print(res)
res = g.send('肉包子')
print(res)
res = g.send('一桶泔水')
print(res)

g.close()
g.send('1111')         # 抛出StopIteration



# 二：
def dog(name):
    print('dog %s 准备吃东西啦' %name)
    food_list = []
    while True:
        # x拿到的是yield接收到的值
        x = yield food_list
        print('dog %s 吃了 %s' %(name, x))
        food_list.append(x)


g = dog('alex')         # 生成器
res = g.send(None)            # 相当于next(g)
print(res)
res = g.send('一根顾头')
print(res)
res = g.send('肉包子')
print(res)
res = g.send('一桶泔水')
print(res)
