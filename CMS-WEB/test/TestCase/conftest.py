import pytest
from test.Comm.Driver import *

@pytest.fixture()
def driver():
    driver=Driver().ChromeDriver()
    print('打开浏览器')
    return driver

# @pytest.fixture()
# def driver_quit():
#     driver.quit()



