from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="OLLLLLLLLD"))
    old_groups = app.group.get_group_list()
    group = Group(name="NEWWWWWWWWWWWW")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(new_groups, key=Group.max_id) == sorted(old_groups, key=Group.max_id)
