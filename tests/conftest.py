import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_base_url():
    browser.config.base_url = 'https://github.com'


@pytest.fixture
def desktop_version():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture
def mobile_version():
    browser.config.window_width = 400
    browser.config.window_height = 700

    yield

    browser.quit()


@pytest.fixture(params=[('desktop', 1920, 1080), ('mobile', 400, 700)])
def browser_setup(request):
    browser.config.window_width = request.param[1]
    browser.config.window_height = request.param[2]

    yield request.param[0]


desktop_only = pytest.mark.parametrize('browser_setup', [('desktop', 1920, 1080)], indirect=True)
mobile_only = pytest.mark.parametrize('browser_setup', [('mobile', 400, 700)], indirect=True)
