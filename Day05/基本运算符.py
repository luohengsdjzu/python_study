# 增量赋值
age = 18
age += 1
print(age)

# 链式赋值
z = y = x = 10
print(x, y, z)
print(id(x), id(y), id(z))

# 交叉赋值
m = 10
n = 20
print(m, n)
m, n = n, m
print(m, n)

# 解压赋值
salaries = [111, 222, 333, ]
mon0, mon1, mon2 = salaries
print(mon0, mon1, mon2)
x, y, *_ = salaries
print(x, y)
*_, y, z = salaries
print(y, z)
x, *_, z = salaries
print(x, z)

# 解压字典默认解压的是key
d = {'a': 1, 'b': 2, 'c': 3}
x, y, z = d
print(x, y, z)
