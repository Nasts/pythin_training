# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group", header="new group", footer="new group"))
    app.group.edit_first_group(Group(name="new edit group", header="new edit group", footer="new edit group"))


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    app.group.edit_first_group(Group(name="change new edit group"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="new group"))
    app.group.edit_first_group(Group(header="change new header group"))
