# 函数嵌套
# 1、函数的嵌套调用，在调用一个函数的过程中又调用其他函数
def max2(a, b):
    if a > b:
        return a
    else:
        return b

def max(a, b, c, d):
    res1 = max2(a, b)
    res2 = max2(res1, c)
    res3 = max2(res2, d)
    return res3


print(max(1, 2, 3, 4))


# 2、函数的嵌套定义：在函数内定义函数
def circle(radius, action=0):
    from math import pi
    def area(radius):
        return pi*(radius**2)
    def perimiter(radius):
        return 2*pi*radius

    if action == 0:
        return perimiter(radius)
    elif action == 1:
        return area(radius)

circle(33, action=0)


