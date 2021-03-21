from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name for edition"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    index = old_groups.index(random_group)
    group = Group(name="New Group Name", header="New Header", footer="New Footer")
    app.group.edit_group_by_id(group, random_group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.max_id) == sorted(app.group.get_group_list(), key=Group.max_id)
