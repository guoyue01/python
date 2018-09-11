from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Login_page(object):
    username=(By.CSS_SELECTOR,'body > div > div.login-main > div > form > div:nth-child(2) > div > div > input')
    password=(By.CSS_SELECTOR,'body > div > div.login-main > div > form > div:nth-child(3) > div > div > input')
    login_button=(By.CSS_SELECTOR,'body > div > div.login-main > div > form > div.el-form-item.btn-item.el-form-item--feedback > div > button > span')

class Shop_page(object):

    shop=(By.XPATH,'/html/body/div/div[2]/div/div/ul/li[1]/section/div/div/div/a')
    pageNo=(By.XPATH,'/html/body/div/div[2]/div/div/div/ul/div/div/input')
    pageNext=(By.XPATH,'/html/body/div/div[2]/div/div/div/ul/li[4]')

    ##根据城市名称选择店铺！！

class HomeAPP_page(object):
    创建页面 = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div/button[2]/span')
    页面属性 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]/div/div/button[1]')
    编辑 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]/div/div/button[2]')
    复制 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]/div/div/button[3]')
    上线 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]/div/div/button[5]')
    设置白名单 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[1]/div/button[3]')

    def CreatAPPHomepage(self):
        页面名称 = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/input')
        最小版本号 = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input')
        提交 = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]')
        取消 = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]')

    def CopyAPPHomepage(self):
        页面名称 = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/form/div[1]/div/div/input')
        最小版本号 = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div[2]/form/div[2]/div/div/input')
        提交 = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div[3]/div/button[2]')
        取消 = (By.XPATH,'/html/body/div[3]/div[2]/div/div/div[3]/div/button[1]')

    def whiteCode(self,phone=''):
        输入号码 = (By.XPATH,'/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/form/div[1]/div/div/input')
        添加 = (By.XPATH,'/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/form/div[2]/div/div/button')
        '删除指定电话的白名单???'
        删除 = (By.XPATH,'')
        关闭 = (By.XPATH,'/html/body/div[4]/div[2]/div/div/div/div/div[3]/button')



    def EditAPPHomepage(self):
        返回 = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/button[1]')
        保存草稿 = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/button[2]')
        预览发布 = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/button[3]/span/span')
        发布上线 = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/button[3]/span/span')

        #图片类
        轮播图 = (By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/section/div/div[1]/div[2]/ul/li[1]/div[1]/div/img')
        #删除组件 = (By.XPATH,'//*[@id="275df5cc-9763-4eb7-b269-b938f2aa5e55"]/span/i')
        #??'//*[@id="%s"]/span/i' %id

if __name__=='__main__':
    driver = webdriver.Chrome()
    base_url = 'http://cms-web.qafc.ops.com/client/login'
    driver.get(base_url)
    driver.maximize_window()

    try:
     driver.find_element(*Login_page.username).send_keys('xiansheng')
     driver.find_element(*Login_page.password).send_keys('xiansheng123')
     driver.find_element(*Login_page.login_button).click()
     time.sleep(1)
     driver.find_element(*Shop_page.shop).click()
     time.sleep(1)
     driver.find_element(*HomeAPP_page.createHomePage).click()

     a=driver.find_element(*HomeAPP_page.homePageName)
     a.clear()
     a.send_keys('web_test')

     driver.find_element(*HomeAPP_page.minVersion).send_keys('1.1.1')
     driver.find_element(*HomeAPP_page.提交).click()

    except BaseException as e:
        print('元素定位出错！',e)

    finally:
     time.sleep(5)
     driver.quit()

