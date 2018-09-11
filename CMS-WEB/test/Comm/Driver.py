from selenium import webdriver
from test.Data.environment import *
class Driver(object):
    def ChromeDriver(self,environment ='QAFC'):
        url=CMS_Environment().cms_web_baseurl[environment]
        driver=webdriver.Chrome()
        driver.get(url)
        return driver

    def FirefoxDriver(self):
        driver=webdriver.Firefox()
        return driver