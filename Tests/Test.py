from selenium import webdriver
import unittest
import pytest
from Pages.searchPage import SearchPage
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()


def testing_search():

    driver.get("https://google.ru")

    search = SearchPage(driver)
    search.enter_searchword("Volo")
    search.click_search()

    driver.close()
    driver.quit()

    print("Test Completed")


if __name__ == '__main__':
    testing_search()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Cronos/Desktop/POMProject/report'))
