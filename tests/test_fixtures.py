from pages.main_page import main_page

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


def test_github_desktop(desktop_version):
    main_page.open()
    main_page.desktop_button_sign_in()
    main_page.should_have_text()


def test_github_mobile(mobile_version):
    main_page.open()
    main_page.mobile_button_sign_in()
    main_page.should_have_text()
