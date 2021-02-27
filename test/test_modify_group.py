from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="OLLLLLLLLD"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="NEWWWWWWWWWWWW"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)