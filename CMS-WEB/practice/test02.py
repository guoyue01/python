'''
2018-06-06
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
I = int(input('请输入利润（万元）：'))
a = [100, 60, 40, 20, 10, 0]
b = [0.001, 0.015, 0.03, 0.05, 0.075, 0.1]

print(a[::-1],b[::-1])
sum = 0
for i in range(0,6):
    if I > a[i]:
        sum = sum+(I-a[i])*b[i]
        I = a[i]

print(sum)

# I = int(input('请输入利润（万元）：'))
# a = [0, 10, 20, 40, 60, 100]
# b = [0.1, 0.075, 0.05, 0.03, 0.015, 0.001]
# k = {
#     0: 0.1*I,
#     10: 1+(I-10)*0.075,
#     20: 1.75+(I-20)*0.05,
#     40: 2.75+(I-40)*0.03,
#     60: 3.35+(I-60)*0.015,
#     100: 3.95+(I-100)*0.001
#      }
# for i in range(0,6):
#     if i>=a[i]:
#         sum

'''
思考：从最大值开始做比较，因为真个题目的规则界限就是较大的值，如果给先跟最大值比较之后，
那就会简洁
'''




