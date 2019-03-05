from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver_win32/chromedriver.exe')
driver.get('https://www1.shalom-house.jp/komon/login.aspx')

driver.save_screenshot('screenshot1.png')

txtID = driver.find_element(by=By.ID, value="txtID")
txtID.send_keys("B0576010")

txtPsw = driver.find_element(by=By.ID, value="txtPsw")
txtPsw.send_keys("bznuw3")

btnLogin = driver.find_element(by=By.ID, value="btnLogin")
btnLogin.click()

driver.save_screenshot('screenshot2.png')

time.sleep(3)

driver.close()
driver.quit()
