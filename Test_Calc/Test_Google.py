from PageObject.GooglePages import SearchHelper


def test_google_calc(browser):
    test_data = ('1*2-3+1', '0')
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word('Калькулятор')
    google_main_page.enter_equality(test_data[0], browser)
    google_main_page.check_data(test_data[0], test_data[1])




