import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "D:\selenium\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("https://the-internet.herokuapp.com/")
        title = driver.title
        print('assert title home:')
        self.assertTrue(title == "The Internet")

        click_Auth = driver.find_element_by_xpath('//*[@id="content"]/ul/li[21]/a')
        click_Auth.click()

        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")

        driver.find_element_by_class_name("radius").click()

        name = driver.find_element_by_tag_name("h2")
        print(name.text)

if __name__ == "__main__":
    unittest.main()