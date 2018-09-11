'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，
然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
'''
from practice.year import *
y = int(input('请输入年：'))
mouth = int(input('请输入月份：'))
day = int(input('请输入日：'))
md = {1: 31, 2: 0, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days = day
if mouth > 2:
    if year(y) == 1:
        md[2] = 29
    else:
        md[2] = 28
for i in range(1, mouth):
    days = md[i]+days
    #print(days)
print(days)








