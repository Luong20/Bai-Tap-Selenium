from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "D:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')
title = driver.find_element_by_id("text-22-sub_row_1-0-1-1-0")
print(title.text)

time.sleep(5)
driver.close()

