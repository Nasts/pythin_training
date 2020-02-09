# -*- coding: utf-8 -*-
import random

import allure

from model.group import Group


# def test_delete_first_group(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.delete_first_group()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[0:1] = []
#     assert old_groups == new_groups


def test_delete_some_group(app, db, check_ui):
    with allure.step("Given a group list"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step("When I choice a group from the list"):
        group = random.choice(old_groups)
    with allure.step("Then I delete a group by id"):
        app.group.delete_group_by_id(group.id)
    with allure.step("Then the new group list is equal to the old list with deleted group"):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)