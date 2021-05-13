
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "D:\selenium\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("http://practice.automationtesting.in/")
        title = driver.title
        driver.maximize_window()
        name = driver.find_element_by_id("text-22-sub_row_1-0-1-1-0")
        print(name.text)
        self.assertTrue(title == "Automation Practice Site")


if __name__ == "__main__":
    unittest.main()

