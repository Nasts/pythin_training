# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group


# функция, которая инициализирует фикстуру
@pytest.fixture
def app(request):
    # создаем фикстуру, т.е. объект типа Application
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="new group", header="new group", footer="new group"))
    app.rerurn_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.rerurn_to_groups_page()
    app.session.logout()
