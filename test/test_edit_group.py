# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new edit group", header="new edit group", footer="new edit group"))
    app.session.logout()
