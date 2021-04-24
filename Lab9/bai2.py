from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "D:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')

time.sleep(5)
driver.close()