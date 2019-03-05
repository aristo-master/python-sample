from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver_win32/chromedriver.exe')
driver.get('https://www.yahoo.co.jp/')

assert "Python" in driver.title

time.sleep(3)

driver.close()
driver.quit()
