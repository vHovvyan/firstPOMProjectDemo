from selenium.webdriver.common.by import By

class SearchPageLocators:

    searchTextBoxName = (By.NAME, "q")
    searchButtonName = (By.NAME, "btnK")
    xpathLocators = (By.XPATH, './/div[@class="yuRUbf"]/a')
    serachLenguge = (By.LINK_TEXT, "русский")
