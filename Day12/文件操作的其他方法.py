#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# 1.读相关操作
# readline: 一次读取一行
# with open(r'g.txt', mode='rt', encoding='utf-8') as f:
#     # res1 = f.readline()
#     # res2 = f.readline()
#     # print(res1)
#     # print(res2)
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)

# readlines
# with open(r'g.txt', mode='rt', encoding='utf-8') as f:
#     res = f.readlines()
#     print(res)

# 2.写相关操作
# with open(r'h.txt', mode='wt', encoding='utf-8') as f:
#     l = ['111', '222', '333']
#     f.writelines(l)


# 补充一：如果是纯英文字符，可以直接加前缀b得到bytes类型
# l = [b'111aaa1\n', b'222nb', b'33eeee']

# 补充二：'上'.encode('utf-8')等同于bytes('上'，encoding='utf-8')
# with open(r'g.txt', mode='wb') as f:
#     l = [
#         bytes('上', encoding='utf-8'),
#          bytes('下', encoding='utf-8'),
#         bytes('左', encoding='utf-8'),
#         bytes('右', encoding='utf-8')
#          ]
#     f.writelines(l)

# 3.flush
with open(r'g.txt', mode='wt', encoding='utf-8') as f:
    f.write('哈哈哈')
    f.flush()

# 4.了解
with open(r'g.txt', mode='wt', encoding='utf-8') as f:
    print(f.readable())     # 判断文件是否可读
    print(f.writable())     # 判断文件是否可写
    print(f.encoding)       # 文件的编码
    print(f.name)           # 文件名
    print(f.closed)         # 文件是否关闭
print(f.closed)
