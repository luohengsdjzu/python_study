#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# with open(r'a.txt', mode='r+t', encoding='utf-8') as f:
#     f.seek(9,0)
#     f.write('<男妇女主任>')

# 方式一：文本编辑采用的就是这种方式(先读出来在内存修改，再写回磁盘)
with open('c.txt', mode='rt', encoding='utf-8') as f:
    res = f.read()
    data = res.replace('we', 'they')

with open('c.txt', mode='wt', encoding='utf-8') as f:
    f.write(data)

# 方式二：
import os

with open('c.txt', mode='rt', encoding='utf-8') as f,\
    open('.c.txt.swap', mode='wt', encoding='utf-8') as f1:
    for line in f:
        f1.write(line.replace('they', 'we'))
os.remove('c.txt')
os.rename('.c.txt.swap', 'c.txt')

# 比较方式一与方式二：
# 方式一占用内存空间大，节约磁盘空间；方式二节约内存空间，占用磁盘空间比较大
