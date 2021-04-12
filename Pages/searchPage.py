from Locators.locators import Locators
from Libs.lib import Lib


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

        self.searchTextBoxName = Locators.searchTextBoxName
        self.searchButtonName = Locators.searchButtonName

    def enter_searchword(self, search_word):
        self.driver.find_element_by_name(self.searchTextBoxName).clear()
        self.driver.find_element_by_name(self.searchTextBoxName).send_keys(search_word)

    def click_search(self):
        self.driver.find_element_by_name(self.searchButtonName).click()
        links = self.driver.find_elements_by_xpath('.//div[@class="yuRUbf"]/a')
        lib = Lib()
        lib.writeToFile(links)
