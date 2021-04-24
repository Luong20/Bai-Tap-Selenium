from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "D:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://the-internet.herokuapp.com/')

click_Auth = driver.find_element_by_xpath('//*[@id="content"]/ul/li[21]/a')
click_Auth.click()

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

driver.find_element_by_class_name("radius").click()

title = driver.find_element_by_tag_name("h2")
print(title.text)

time.sleep(5)
driver.close()