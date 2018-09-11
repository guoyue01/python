'''
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
输出前十个
'''
def f(n):
    l = [0, 1]
    sum = 0
    if n == 1:
        print('sum : %s , list : %s' %(sum, l.pop()))
    elif n == 2:
        print('sum : %s , list : %s' %(l[1]+l[0], l))
    elif n > 2:
        for i in range(1,n):
            sum = sum + l[i]
            # print('sum')
            # print('l[i]',l[i])
            # print('l[i-1]',l[i-1])
            l.append(l[i]+l[i-1])
            l[i+1]=l[i]+l[i-1]
    print('sum : %s , list : %s' %(sum, l))

f(6)

