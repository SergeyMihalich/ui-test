from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class GoogleSeacrhLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.XPATH, '//input[@class="gLFyf gsfi"]')
    LOCATOR_GOOGLE_TITLE = (By.XPATH, '//title[contains(text(), "Google")]')
    LOCATOR_GOOGLE_EQUALLY = (By.XPATH, '//*[@id="cwos"]')
    LOCATOR_GOOGLE_EQUALITY = (By.XPATH, '//*[@jsname="ubtiRe"]')
    LOCATOR_GOOGLE_BUTTON = {
        '(': '//div[@jsname="j93WEe"]',
        ')': '//div[@jsname="qCp9A"]',
        '%': '//div[@jsname="F0gbu"]',
        '/': '//div[@jsname="WxTTNd"]',
        '*': '//div[@jsname="YovRWb"]',
        '-': '//div[@jsname="pPHzQc"]',
        '+': '//div[@jsname="XSr6wc"]',
        '1': '//div[@jsname="N10B9"]',
        '2': '//div[@jsname="lVjWed"]',
        '3': '//div[@jsname="KN1kY"]',
        '4': '//div[@jsname="xAP7E"]',
        '5': '//div[@jsname="Ax5wH"]',
        '6': '//div[@jsname="abcgof"]',
        '7': '//div[@jsname="rk7bOd"]',
        '8': '//div[@jsname="T7PMFe"]',
        '9': '//div[@jsname="XoxYJ"]',
        '0': '//div[@jsname="bkEvMb"]',
        '.': '//div[@jsname="YrdHyf"]',
        '=': '//div[@jsname="Pt8tGc"]',
    }


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word, Keys.ENTER)
        return search_field

    def check_title(self):
        title = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_TITLE, time=2)
        return title.tag_name

    def enter_equality(self, equality, browser):
        search_calc = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_EQUALLY)
        action = ActionChains(browser)
        for i in equality:
            action.click(search_calc).send_keys(i)
        action.send_keys(Keys.ENTER).perform()

    def enter_equality_battons(self, equality, browser):
        search_calc = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_EQUALLY)
        for i in equality:
            browser.find_element_by_xpath(GoogleSeacrhLocators.LOCATOR_GOOGLE_BUTTON[i]).click()

    def check_equally(self):
        equally = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_EQUALLY)
        return equally

    def check_equality(self):
        equality = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_EQUALITY)
        return equality
