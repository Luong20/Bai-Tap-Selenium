from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "D:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('http://practice.automationtesting.in/')

click_account = driver.find_element_by_id("menu-item-50")
click_account.click()

email = driver.find_element_by_name("email")
email.send_keys("luong@gmail.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("imall219mFu@Q")

register = driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]')
register.click()

time.sleep(5)
driver.close()