# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
