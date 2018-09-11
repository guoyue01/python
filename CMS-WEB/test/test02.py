from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from test.Data.environment import *
from test.Data.Page.Element_LoginPage import *
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
base_url = 'http://cms-web.qafc.ops.com/client/login'
driver.get(base_url)
try:
    driver.find_element(*Login_page().username).send_keys('siji')
    driver.find_element(*Login_page().password).send_keys('siji123')
    a=driver.find_element(By.XPATH,'/html/body/div/div[2]/div/form/div[4]/div/button').click()
    time.sleep(1)
    #driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/ul/li[1]/section/div/div/div')
    #
    a=driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/ul/li[1]/section/div/div/div/a')
    ActionChains(driver).move_to_element(a).perform()
    print('aaaa',a.text)
    a.click()
    #b=By.XPATH,'/html/body/div/div[2]/div/div/ul/li[1]/section/div/div/div/a'
    time.sleep(3)
except BaseException as e:
    print('error',e)
finally:
    driver.quit()




