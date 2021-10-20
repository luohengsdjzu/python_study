#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# with会自动进行上下文管理，在结束之后自动调用f.close()
# with open('a.txt', mode='rt') as f:    # f = open('a.txt', mode='rt')
#     res = f.read()
#     print(res)


with open('a.txt', mode='rt') as f1, \
        open('b.txt', mode='rt') as f2:
    res1 = f1.read()
    res2 = f2.read()
    print(res1)
    print(res2)
