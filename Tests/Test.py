from selenium import webdriver
import unittest
import pytest
from Pages.searchPage import SearchPage
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Cronos/Desktop/POMProject/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def testing_search(self):
        driver = self.driver
        driver.get("https://google.ru")

        search = SearchPage(driver)
        search.enter_seachword("Volo")
        search.click_search()

        driver.close()
        driver.quit()

        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Cronos/Desktop/POMProject/report'))
