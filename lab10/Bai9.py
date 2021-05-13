from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "D:\selenium\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get('https://itmscoaching.herokuapp.com/form?fbclid=IwAR1YYSIdGp7M8sTWrIdOpPbMqbSu7Ixo7vMtzn_iZk10XZhvfcWwDf4uOhk')
        title = driver.title
        self.assertTrue(title == "Formy")
        firstname = driver.find_element_by_id("first-name")
        lastname = driver.find_element_by_id("last-name")
        job = driver.find_element_by_id("job-title")
        education = driver.find_element_by_id("radio-button-3")
        sex = driver.find_element_by_id("checkbox-2")
        experience = driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]')
        date = driver.find_element_by_id("datepicker")

        firstname.send_keys("Binh")
        lastname.send_keys("Nguyen")
        job.send_keys("Tester")
        education.click()
        sex.click()
        experience.click()
        date.send_keys("20/07/2011")

        driver.find_element_by_class_name("btn-primary").click()

if __name__ == "__main__":
    unittest.main()

