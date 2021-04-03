from Locators.locators import Locators


class SearchPage():
    def __init__(self, driver):
        self.driver = driver

        self.searchTextBoxName = Locators.searchTextBoxName
        self.searchButtonName = Locators.searchButtonName

    def enter_seachword(self, search_word):
        self.driver.find_element_by_name(self.searchTextBoxName).clear()
        self.driver.find_element_by_name(self.searchTextBoxName).send_keys(search_word)

    def click_search(self):
        self.driver.find_element_by_name(self.searchButtonName).click()
        links = self.driver.find_elements_by_xpath('.//div[@class="yuRUbf"]/a')
        print(links)
        with open('test_file.txt', 'a') as f:
            for link in links:
                href = link.get_attribute('href')
                f.write(str(href) + "\n")
