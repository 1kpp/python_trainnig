from pytest_bdd import given, when, then
from model.group import Group
import random

@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header> and <footer>', target_fixture="new_group")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('i add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with the added one')
def verify_group_is_added(db, group_list, new_group):
    old_group_list = group_list
    new_group_list = db.get_group_list()
    old_group_list.append(new_group)
    assert sorted(new_group_list, key=Group.max_id) == sorted(old_group_list, key=Group.max_id)

@given('a non-empty group list',target_fixture='non_empty_group_list')
def non_empty_group_list(db, app):
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name='Group for deletion'))
    return db.get_group_list()

@given('a random group from the list', target_fixture='random_group')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('i delete a group from the group list')
def delete_random_group_from_the_list(random_group, app):
    app.group.delete_group_by_id(random_group.id)

@then('The new list becomes less then old group list on one')
def vrify_group_deleted(db, non_empty_group_list, random_group, check_ui, app):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.max_id) == sorted(app.group.get_group_list(), key=Group.max_id)
