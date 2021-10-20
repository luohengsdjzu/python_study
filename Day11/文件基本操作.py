#!/usr/bin/env python
# coding:utf-8

# 1、打开文件
# windows路径分隔符问题
# open('c:\a\nb\c\d.txt')   此时\a结合响铃、\n结合回车
# 解决方案一：推荐
# open(r'c:\a\nb\c\d.txt')    # rawstring 代表原始字符串
# 解决方案二：
# open('c:/a/nb/c/d.txt')     # 全部用左斜杠分割

f = open(r'aaa.txt', mode='rt', encoding='utf-8')
# print(f)
# 2、操作文件：读/写文件，应用程序对文件的读写请求都是在向操作系统发起系统调用，然后由操作系统
# 控制硬盘把输入读入内存、或者写入硬盘
res = f.read()
# print(res)
# 3、关闭文件
f.close()       # 回收操作系统资源
print(f)
f.read()        # 变量f存在，但是不能再读了

