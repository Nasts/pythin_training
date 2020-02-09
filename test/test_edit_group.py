# -*- coding: utf-8 -*-
import random

import allure

from model.group import Group


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new group"))
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step("When I choice a group from the list"):
        edit_group = random.choice(old_groups)
    group = Group(name="New group edit", id=edit_group.id)
    with allure.step("Then I edit a group by id"):
        app.group.edit_group_by_id(edit_group.id, group)
    with allure.step("Then the new group list is equal to the old list"):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[old_groups.index(edit_group)] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_edit_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="new group", header="new group", footer="new group"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="new edit group", header="new edit group", footer="new edit group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


# def test_edit_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="new group"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="change new edit group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="new group"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(header="change new header group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
