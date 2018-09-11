from selenium import webdriver
from test.Data.environment import *
from test.Data.Page.Element_LoginPage import *
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging
'''
2018-09-03
guoyue
登录系统
'''
#logging.basicConfig(format='%(asctime)s %(message)s',filename='/Users/guoyue/PycharmProjects/CMS-WEB/test/Log/log01',level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO)


class Login(object):
    def __init__(self, type='tubobo',environment='QAFC'):
        self.environment = environment
        self.url = CMS_Environment().cms_web_baseurl[self.environment]
        self.username = CMS_Account().data
        self.password = CMS_Account().data
        self.driver = webdriver.Chrome()
        self.type=type

    def login(self):
        self.driver.get(self.url)

        try:
            self.driver.find_element(*Login_page().username).send_keys(self.username[self.type]['username'])
            self.driver.find_element(*Login_page().password).send_keys(self.password[self.type]['password'])
            self.driver.find_element(*Login_page().login_button).click()
            logging.info('%s登录url:%s' %(self.type, self.url))
            time.sleep(3)

        except BaseException as e:
            print('登录出现错误:',e)
            logging.error('出现错误:%s' %e)
            self.driver.quit()

    def logout_shopPage(self):
        try:
            logout =self.driver.find_element(*Login_page().logout_shopPage)
            ActionChains(self.driver).move_to_element(logout).perform()
            time.sleep(1)
            self.driver.find_element(*Login_page().logout_button_shopPage).click()
            logging.info('%s用户登出' %self.type)
        except BaseException as e:
            logging.error('登出出现错误：%s' %e)
            self.driver.quit()



if __name__=='__main__':
    login=Login()
    login.login()
    login.logout_shopPage()





