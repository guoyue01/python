import pytest
from test.Comm.Driver import *
import allure
from test.Data.Action.Action_LoginPage import *
from selenium import webdriver

'''
2018-09-04
guoyue
登录测试
'''
data01 = [
    {'username': 'siji', 'password': 'siji123'},
    {'username': 'xiansheng', 'password': 'xiansheng123'}
]
data02 = [
    {'username': '', 'password': 'siji123'},
    {'username': 'xiansheng', 'password': ''},
    {'username': 'si11', 'password': 'siji123'},
    {'username': 'xiansheng', 'password': 'siji111'}
]


class TestLogin(object):
    def setup(self):
        print('开启浏览器')
        self.driver = Driver().ChromeDriver()

    #@allure.story('登录测试')
    @pytest.mark.parametrize('data01', data01)
    def test_case01(self, data01):
        #self.driver=driver
        loginpage = LoginPage(self.driver)
        loginpage.loginpage(username=data01['username'], password=data01['password'])
        time.sleep(3)
        shopPage=ShopPage(self.driver)
        assert'进入' in shopPage.assert_shopPage() ,'登录失败'

    #@allure.story('异常登录测试')
    @pytest.mark.parametrize('data02', data02)
    def test_case02(self, data02):
        self.driver = driver
        loginpage = LoginPage(self.driver)
        loginpage.loginpage(username=data02['username'], password=data02['password'])
        time.sleep(3)
        assert loginpage.assert_Loginpage() == '登录', '异常登录测试失败'
    #
    def teardown(self):
        print('关闭浏览器')
        self.driver.quit()






