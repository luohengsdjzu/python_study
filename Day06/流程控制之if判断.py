#!/usr/bin/env python
# -*- encoding:utf-8 -*-


'''
语法1：
if  条件:
    代码1
    代码2
'''
age = 18
is_beautiful = True
star = '水平座'

if 16 < age < 20 and is_beautiful and star == '水平座':
    print('我喜欢，我们在一起吧。。。')
print('其他代码。。。')

'''
语法2:
if  条件:
    代码1
    代码2
else:
    代码1
    代码2
'''

age = 60
is_beautiful = True
star = '水平座'

if age > 16 and age < 20 and is_beautiful and star == '水平座':
    print('我喜欢，我们在一起吧。。。')
else:
    print('拜拜')

print('其他代码。。。')

'''
语法3:
if  条件1:
    代码1
    代码2
elif 条件2:
    代码1
    代码2
elif 条件3:
    代码1
    代码2
'''
# score = input('请输入你的成绩:')
# score = int(score)
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 70:
#     print('普通')

'''
语法4:
if  条件1:
    代码1
    代码2
elif 条件2:
    代码1
    代码2
elif 条件3:
    代码1
    代码2
else:
    代码1
    代码2
'''

score = input('请输入你的成绩:')
score = int(score)
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('普通')
else:
    print('很差')
