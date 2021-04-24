from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "D:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.set_window_size(1040, 1080)
driver.get('http://practice.automationtesting.in/')
html_source = driver.page_source
print(html_source)

time.sleep(5)
driver.close()