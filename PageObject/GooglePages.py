from PageObject.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from colorama import Fore


class GoogleSeacrhLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.XPATH, '//input[@class="gLFyf gsfi"]')
    LOCATOR_GOOGLE_EQUALLY = (By.XPATH, '//*[@id="cwos"]')
    LOCATOR_GOOGLE_EQUALITY = (By.XPATH, '//*[@jsname="ubtiRe"]')


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word, Keys.ENTER)
        return search_field

    def enter_equality(self, equality, browser):
        search_calc = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_EQUALLY)
        action = ActionChains(browser)
        for i in equality:
            action.click(search_calc).send_keys(i)
        action.send_keys(Keys.ENTER).perform()

    def check_equally(self):
        equally = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_EQUALLY)
        return equally.text

    def check_equality(self):
        equality = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_EQUALITY)
        return equality.text

    def check_data(self, test_data, equally):
        test_data += '='
        equality = []
        for i in test_data:
            if i == '*':
                equality += '×'
            else:
                equality += i
        result = str(' '.join(equality))
        assert self.check_equality() == result, Fore.RED + 'формула в строке памяти не соответствует ранее введенному значению'
        assert self.check_equally() == equally, Fore.RED + 'отображается неверный ответ в строке результата'
