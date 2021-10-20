#!/usr/bin/env python
# -*- encoding:utf-8 -*-


'''
控制文件读写内容的模式
t:
    1、读写都是以字符串（unicode）为单位
    2、只能针对文本文件
    3、必须指定字符编码
b:binary模式
    1、读写都是以bytes为单位
    2、可以针对所有文件
    3、一定不能指定字符编码
总结：
    1、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要手动编码解码
    2、针对非文本文件（如图片、视频、音频）只能使用b模式
'''
# t模式只能读文本文件
# with open('test.jpg', mode='r', encoding='utf-8') as f:
#     f.read()    # 硬盘的二进制读入内存->t模式会将读入内存的内容进行decode解码操作


# with open('test.jpg', mode='rb') as f:
#     res = f.read()    # 硬盘的二进制读入内存->b模式下，不做任何转换，直接读入内存
#     print(res, type(res))

# with open('d.txt', mode='rb') as f:
#     res = f.read()
#     print(res, type(res))
#     print(res.decode('utf-8'))
#
# with open(r'e.txt', mode='wb') as f:
#     f.write('你好hello'.encode('GBK'))
#
# with open(r'f.txt', mode='wb') as f:
#     f.write('你好hello'.encode('utf-8'))

# 文件拷贝工具
# src_file = input('源文件路径>>:').strip()
# dst_file = input('目标文件路径>>:').strip()
# with open(r'{}'.format(src_file), mode='rb') as f1, \
#     open(r'{}'.format(dst_file), mode='wb') as f2:
#     for line in f1:
#         f2.write(line)


# 循环读取文件
# 方式一：自己控制每次读取的数据量
# with open(r'test.jpg', mode='rb') as f:
#     while True:
#         res = f.read(1024)
#         if len(res) == 0:
#             break
#         print(len(res))

# 方式二：以行为单位读，当一行内容过长时会导致一次性读入内容的数据量过大
# with open(r'g.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         print(line)
#
# with open(r'test.jpg', mode='rb') as f:
#     for line in f:  # 二进制仍然按照\n分割每一行的
#         print(line)

with open(r'g.txt', mode='rt', encoding='utf-8') as f:
    # res1 = f.readline()
    # res2 = f.readline()
    # print(res1)
    # print(res2)
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

