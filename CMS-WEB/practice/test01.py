'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

count = 0
for i in range(1,5,1):
    for j in range(1,5):
        for k in range(1,5,1):
            if (i != j)and (i != k)and(j != k):
                count = count+1
                print('%s : %s' %(count, i*100+j*10+k))

'郭越，2018-09-06'