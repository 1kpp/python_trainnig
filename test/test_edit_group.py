from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name for edition"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="New Group Name", header="New Header", footer="New Footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
