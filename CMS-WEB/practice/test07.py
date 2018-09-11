'''
题目：将一个列表的数据复制到另一个列表中。
思考多种方式复制列表（注意不是改变引用）
'''
a=[1,2,3,4]
'方法1'
a1=a[:]
print(a is a1,'a1: ',a1)

'方法2'
a2=a.copy()
print(a is a2,'a2: ',a2 )

'方法3'
a3=[]
a3=a3+a
print(a is a3, 'a3: ', a3)

'方法4'
a4=[]
for i in a:
    a4.append(i)

print(a is a4, 'a4: ', a4)

'方法5'
a5 = [i for i in a]
print(a is a5, 'a5: ', a5)



