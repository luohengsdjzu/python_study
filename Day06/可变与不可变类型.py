# 可变与不可变类型

# int是不可变类型
x = 10
print(id(x))
x = 11
print(id(x))

# float是不可变类型
x = 3.1
print(id(x))
x = 3.2
print(id(x))

# str是不可变类型
x = 'abc'
print(id(x))
x = 'edf'
print(id(x))

# list是可变类型
l = ['aaa', 'bbb', 'ccc']
print(id(l))
l[0] = 'AAA'
print(id(l))

# dict是可变类型
dic = {'k1': 111, 'k2': 222}
print(id(dic))
dic['k1'] = 333
print(id(dic))

# bool是不可变类型
x = True
print(id(x))
x = False
print(id(x))

dic = {[1, 2, 3]: 0}


