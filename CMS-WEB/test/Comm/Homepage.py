from selenium import webdriver
from test.Data.environment import *
from test.Comm.login import *
'''
2018-09-04
guoyue
创建/编辑/删除/上线首页
'''
class Homepage(object):
    def __init__(self,type='tubobo',environment ='QAFC'):
        self.environment = environment
        login=Login(self.environment)
        self.type=type
        login.login(self.type)


    def createHomepage(self):
        ''