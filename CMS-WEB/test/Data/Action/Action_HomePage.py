from test.Comm.Driver import *
from test.Data.Page.Element_HomePage import *
'''
2018-09-06
guoyue
创建/编辑/删除/复制首页
'''
class HomePage_APP (object):
    def __init__(self):
        self.driver = Driver().ChromeDriver()

    def 点击创建APP首页按钮(self):
        createHomepage = self.driver.find_element(*APPHomepage().创建页面)
        createHomepage.click()

    def 创建APP首页的数据(self, pageName, minVersion):
        pagename = self.driver.find_element(*CreatAPPHomepage().页面名称)
        pagename.clear()
        pagename.send_keys(pageName)
        minversion = self.driver.find_element(*CreatAPPHomepage().最小版本号)
        minversion.clear()
        minversion.send_keys(minVersion)

    def 提交创建APP首页(self):
        self.driver.find_element(*CreatAPPHomepage().提交)

    def 取消创建APP首页(self):
        self.driver.find_element(*CreatAPPHomepage().取消)

    def 点击页面属性(self):
        self.driver.find_element(*APPHomepage().页面属性).click()

    def 填入页面属性的数据(self):
        ''





