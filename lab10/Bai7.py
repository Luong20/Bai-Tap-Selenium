
import unittest
from selenium import webdriver
import time


class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "D:\selenium\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("http://practice.automationtesting.in/")
        title = driver.title
        self.assertTrue(title == "Automation Practice Site")

        click_account = driver.find_element_by_id("menu-item-50")
        click_account.click()

        email = driver.find_element_by_name("email")
        email.send_keys("luongeeee@gmail.com")
        password = driver.find_element_by_id("reg_password")
        password.send_keys("imall219mFu@Q")

        time.sleep(5)

        driver.find_element_by_name('register').click()


if __name__ == "__main__":
    unittest.main()