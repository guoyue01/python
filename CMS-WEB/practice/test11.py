'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2, 3,5,8, 13,21....
思考：其实就是斐波那契数列
'''

l = []
for i in range(0,13):
    print('第%d个月：' % i, end='')
    if i <2:
        l.append(1)
        print('兔子数量：%s' % l[i])
    else:
        l.append(l[i-1]+l[i-2])
        print('兔子数量：%s' % l[i])