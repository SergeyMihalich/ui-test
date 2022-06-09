import time

from PageObject.GooglePages import SearchHelper


def test_google_calc(browser):
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word('Калькулятор')
    time.sleep(2)
    element = google_main_page.check_title()
    assert element in "title"
    google_main_page.enter_equality('1*2-3+1=', browser)
    equally = google_main_page.check_equally()
    equality = google_main_page.check_equality()
    time.sleep(2)
    assert equally.text == '0'
    assert equality.text == '1 × 2 - 3 + 1 ='
    google_main_page.refresh()
    google_main_page.enter_equality_battons('1*2-3+1=', browser)
    equally = google_main_page.check_equally()
    equality = google_main_page.check_equality()
    time.sleep(2)
    assert equally.text == '0'
    assert equality.text == '1 × 2 - 3 + 1 ='
