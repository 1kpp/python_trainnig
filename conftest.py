from fixture.application import Application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    password = request.config.getoption("password")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, password=password)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, password=password)
    fixture.session.ensure_login(username="admin", password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--password", action="store", default="secret")
