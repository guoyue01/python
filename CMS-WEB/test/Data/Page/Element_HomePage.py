from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class APPHomepage(object):
    创建页面 = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div/button[2]/span')
    页面属性 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]/div/div/button[1]')
    编辑 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]/div/div/button[2]')
    复制 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]/div/div/button[3]')
    上线 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]/div/div/button[5]')
    设置白名单 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[1]/div/button[3]')

class CreatAPPHomepage(object):
    页面名称 = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/input')
    最小版本号 = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input')
    提交 = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]')
    取消 = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]')


class CopyAPPHomepage(object):
    页面名称 = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/form/div[1]/div/div/input')
    最小版本号 = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/form/div[2]/div/div/input')
    提交 = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div[3]/div/button[2]')
    取消 = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div[3]/div/button[1]')


class WhiteCode(phone=''):
    输入号码 = (By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/form/div[1]/div/div/input')
    添加 = (By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/form/div[2]/div/div/button')
    '删除指定电话的白名单???'
    删除 = (By.XPATH, '')
    关闭 = (By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div[3]/button')


class EditAPPHomepage(object):
    返回 = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/button[1]')
    保存草稿 = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/button[2]')
    预览发布 = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/button[3]/span/span')
    发布上线 = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/button[3]/span/span')

    # 图片类
    轮播图 = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/section/div/div[1]/div[2]/ul/li[1]/div[1]/div/img')
    # 删除组件 = (By.XPATH,'//*[@id="275df5cc-9763-4eb7-b269-b938f2aa5e55"]/span/i')
    # ??'//*[@id="%s"]/span/i' %id


if __name__=='__main__':
    ''

