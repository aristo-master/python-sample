from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver_win32/chromedriver.exe')
driver.get('https://www.yahoo.co.jp/')

assert "Python" in driver.title

driver.close()
driver.quit()
