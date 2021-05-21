from Locators.locators import SearchPageLocators
from Libs.writeToFileLib import Lib
from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):

        self.driver = driver

        #self.searchTextBoxName = Locators.searchTextBoxName
        #self.searchButtonName = Locators.searchButtonName

    def enter_searchWord(self, search_word):
        self.driver.find_element(*SearchPageLocators.searchTextBoxName).clear()
        self.driver.find_element(*SearchPageLocators.searchTextBoxName).send_keys(search_word)

    def click_search(self):
        self.driver.find_element(*SearchPageLocators.searchButtonName).click()
        links = self.driver.find_elements(*SearchPageLocators.xpathLocators)
        
        lib = Lib()
        lib.writeToFile(links)
