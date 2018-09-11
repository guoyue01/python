from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Login_page(object):
    username=(By.CSS_SELECTOR,'body > div > div.login-main > div > form > div:nth-child(2) > div > div > input')
    password=(By.CSS_SELECTOR,'body > div > div.login-main > div > form > div:nth-child(3) > div > div > input')
    login_button=(By.XPATH,'/html/body/div/div[2]/div/form/div[4]/div/button')
    logout_shopPage=(By.XPATH,'/html/body/div/div[1]/div/div[2]/div/div/div[1]')
    logout_button_shopPage=(By.XPATH,'/html/body/div/div[1]/div/div[2]/div/div/div[2]/ul/li')
    logout_button_homePage=(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/ul/li')


class Shop_page(object):

    shopNo1=(By.XPATH,'/html/body/div/div[2]/div/div/ul/li[1]/section/div/div/div/a')
    pageNo=(By.XPATH,'/html/body/div/div[2]/div/div/div/ul/div/div/input')
    pageNext=(By.XPATH,'/html/body/div/div[2]/div/div/div/ul/li[4]')

    ##根据城市名称选择店铺！！

if __name__=='__main__':
    ''





