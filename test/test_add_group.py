# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When i add a group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then the new group list is equal to the old list with the added one'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(new_groups, key=Group.max_id) == sorted(old_groups, key=Group.max_id)
        if check_ui:
            assert sorted(new_groups, key=Group.max_id) == sorted(app.group.get_group_list(), key=Group.max_id)

