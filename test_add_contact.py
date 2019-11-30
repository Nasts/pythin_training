# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    # создаем фикстуру, т.е. объект типа Application
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(
        Contact(first_name="firstname", last_name="last name", address="Moscow", email="test@msk.com",
                mobile="123"))
    app.return_to_home_page()
    app.logout()


def test_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", last_name="", address="", email="",
                                    mobile=""))
    app.return_to_home_page()
    app.logout()


def tearDown(self):
    self.app.destroy()
