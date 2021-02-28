from model.group import Group
from random import randrange


def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name for edition"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Group Name", header="New Header", footer="New Footer")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(new_groups, key=Group.max_id) == sorted(old_groups, key=Group.max_id)
