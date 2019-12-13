# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="new group", header="new group", footer="new group"))
    app.group.edit_first_group(Group(name="new edit group", header="new edit group", footer="new edit group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    app.group.edit_first_group(Group(name="change new edit group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(header="new group"))
    app.group.edit_first_group(Group(header="change new header group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

