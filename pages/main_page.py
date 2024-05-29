from selene import browser, have


class MainPage:
    def open(self):
        browser.open('/')
        return self

    def desktop_button_sign_in(self):
        browser.element('.HeaderMenu-link--sign-in').click()

    def mobile_button_sign_in(self):
        browser.element('.Button--link').click()
        browser.element('.HeaderMenu-link--sign-in').click()

    def should_have_text(self):
        browser.element('.auth-form-header').element('h1').should(have.text('Sign in to GitHub'))


main_page = MainPage()
