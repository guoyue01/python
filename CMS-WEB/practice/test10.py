'''
题目：暂停一秒输出，并格式化当前时间。
'''
import time

localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(localtime)
time.sleep(1)
localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(localtime)