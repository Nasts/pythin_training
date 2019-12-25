import pytest
from fixture.application import Application

fixture = None


# функция, которая инициализирует фикстуру (метод создает фикстуру)
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    password = request.config.getoption("--password")
    if fixture is None:
        # создаем фикстуру, т.е. объект типа Application
        fixture = Application(browser=browser, base_url=base_url, password=password)
    else:
        if not fixture.is_valid(browser=browser, base_url=base_url, password=password):
            fixture = Application()
    fixture.session.ensure_login(username="admin", password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost:8080/addressbook/")
    parser.addoption("--password", action="store", default=None)


