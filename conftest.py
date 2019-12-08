import pytest
from fixture.application import Application

fixture = None


# функция, которая инициализирует фикстуру (метод создает фикстуру)
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        # создаем фикстуру, т.е. объект типа Application
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
