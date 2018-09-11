'''
题目：输出 9*9 乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
'''
'方法1'
for i in range(1, 10):
    for j in range(1, i+1):
        if j == 10:
            break
        print('%s*%s=%s' %(i, j, i*j), end=' ')
    print('')

print('******************************')

'方法2'
for j in range(9):
    i = 1
    j = j + 1
    while(i <= j):
        s = j*i
        print('%dx%d=%d'%(i,j,s),end=' ')
        i = i + 1
    print(' ')