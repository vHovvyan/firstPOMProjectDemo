import sys
import os
import pytest
from selenium import webdriver
from Locators.locators import SearchPageLocators
from Pages.searchPage import SearchPage
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


def testing_search():

    try:
        driver = webdriver.Chrome()
        driver.get("https://google.ru")
        driver.maximize_window()
        driver.find_element(*SearchPageLocators.serachLenguge).click()
        search = SearchPage(driver)
        search.enter_searchWord("Volo")
        search.click_search()
        print("Test Completed")
    finally:

        driver.close()
        driver.quit()