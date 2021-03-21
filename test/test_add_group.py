# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.max_id) == sorted(old_groups, key=Group.max_id)
    if check_ui:
        assert sorted(new_groups, key=Group.max_id) == sorted(app.group.get_group_list(), key=Group.max_id)

