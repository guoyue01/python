import selenium
from test.Data.Page.Element_LoginPage import *
from test.Comm.Driver import *
'''
2018.09.04
guoyue
登录页面的操作行为
'''
class LoginPage(Driver):
    def __init__(self, driver):
        self.driver = driver

    def loginpage(self, username, password):

        self.driver.find_element(*Login_page().username).send_keys(username)
        self.driver.find_element(*Login_page().password).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*Login_page().login_button).click()

        #self.driver.quit()
    def assert_Loginpage(self):
        return self.driver.find_element(*Login_page().login_button).text



class ShopPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.shopNo1 = self.driver.find_element(*Shop_page().shopNo1)

    def shopPage(self):
        self.shopNo1.click()

    def assert_shopPage(self):
        ActionChains(self.driver).move_to_element(self.shopNo1).perform()
        return self.shopNo1.text


if __name__=='__main__':
    data01 =  {'username': 'siji', 'password': 'siji123'}
    driver=Driver().ChromeDriver()
    LoginPage(driver).loginpage(username=data01['username'],password=['password'])
    driver.quit()
    #assert LoginPage(driver).assert_Loginpage() == '登录', '异常登录测试失败'