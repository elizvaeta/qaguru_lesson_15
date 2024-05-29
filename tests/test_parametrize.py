"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
from pages.main_page import main_page
from tests.conftest import desktop_only, mobile_only


@desktop_only
def test_github_desktop(browser_setup):
    main_page.open()
    main_page.desktop_button_sign_in()
    main_page.should_have_text()


@mobile_only
def test_github_mobile(browser_setup):
    main_page.open()
    main_page.mobile_button_sign_in()
    main_page.should_have_text()
