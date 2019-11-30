# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    # создаем фикстуру, т.е. объект типа Application
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(first_name="firstname", last_name="last name", address="Moscow", email="test@msk.com",
                mobile="123"))
    app.session.logout()


def test_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", last_name="", address="", email="",
                               mobile=""))
    app.session.logout()


def tearDown(self):
    self.app.destroy()
