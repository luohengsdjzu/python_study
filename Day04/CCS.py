# -*- encoding:utf-8 -*-

with open(r'C:\Users\luoheng_sdjzu\Desktop\CCS.txt') as f:
    lines = f.readlines()
    s = set()
    for line in lines:
        s.add(line)
    print(len(s))
