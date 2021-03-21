from model.group import Group
import random


def test_modify_some_group_name(app,db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="OLLLLLLLLD"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    index = old_groups.index(random_group)
    group = Group(name="NEWWWWWWWWWWWW")
    app.group.modify_group_by_id(group, random_group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.max_id) == sorted(app.group.get_group_list(), key=Group.max_id)
