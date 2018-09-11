'''
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数。
'''
import time
a = {1: 1, 'a': 'fff', 'd': '2'}
for key in a:
    print(a[key])
    time.sleep(1)
print('bye')