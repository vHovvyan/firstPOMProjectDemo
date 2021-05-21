from selenium.webdriver.common.by import By

class SearchPageLocators:

    searchTextBoxName = (By.NAME, "q")
    searchButtonName = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    xpathLocators = (By.XPATH, './/div[@class="yuRUbf"]/a')
    serachLenguge = (By.LINK_TEXT, "русский")
