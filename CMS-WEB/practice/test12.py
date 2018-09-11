# -*- coding: UTF-8 -*-
'''
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数。
'''
from math import sqrt

l = []
for i in range(101, 201):
    k = int(sqrt(i+1))    #求平方根，取整
    for j in range(2, k+1):
        if i % j == 0:
            break
        else:
            pass
    else:                 #for```else 用法
        l.append(i)
print('素数：', l)
print('一共有%d个素数:' % len(l))

