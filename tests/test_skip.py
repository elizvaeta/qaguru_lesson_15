"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from pages.main_page import main_page


def test_github_desktop(browser_setup):
    if browser_setup != 'desktop':
        pytest.skip('Not desktop version')

    main_page.open()
    main_page.desktop_button_sign_in()
    main_page.should_have_text()


def test_github_mobile(browser_setup):
    if browser_setup != 'mobile':
        pytest.skip('Not mobile version')

    main_page.open()
    main_page.mobile_button_sign_in()
    main_page.should_have_text()
