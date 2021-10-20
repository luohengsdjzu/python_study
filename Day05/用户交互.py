# username = input("请输入你的账号：")
# print(username, type(username))

# 格式化输出
# res = "my name is %s, my age is %s" %('zhang', )
# res = "my name is %(name)s, my age is %(age)s" % {'name': "zhang", 'age': '18'}
# print(res)

# res = "my name is {0} {0} {0}, my age is {1} {1}".format('zhang', 18)
# print(res)

# res = "我的名字是 {name}, 我的年龄是 {age}".format(age=18, name='zhang')
# print(res)

# f格式化输出
name = input('your name:')
age = input('your age:')
res = f'my name is {name}, my age is {age}.'
print(res)
