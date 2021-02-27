from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name for edition"))
    old_groups = app.group.get_group_list()
    group = Group(name="New Group Name", header="New Header", footer="New Footer")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(new_groups, key=Group.max_id) == sorted(old_groups, key=Group.max_id)
