from model.group import Group
from random import randrange


def test_modify_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="OLLLLLLLLD"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="NEWWWWWWWWWWWW")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(new_groups, key=Group.max_id) == sorted(old_groups, key=Group.max_id)
