from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db, check_ui):
    # checks whether there are contacts available. If not - create one
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="Name for deletion"))
    # check whether there are groups available. If not - create one
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="azazazaz"))
    # check if there are groups with contacts if not - add random contact to random group
    if len(db.get_contacts_groups_table()) == 0:
        group = random.choice(db.get_group_list())
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group( contact.id, group.id)
    # look for group with contact
    group_with_contact = db.find_group_with_contact()
    # take random contact from group
    random_contact_from_group = db.show_random_contact_from_group(group_with_contact)
    # delete choosen contact from group
    app.contact.delete_contact_from_group(group_with_contact.id)
    # take all the contacts left in group after deletion
    all_contacts_after_deletion = db.show_all_contacts_in_group(group_with_contact)
    # check whether deleted contact is still in group
    assert random_contact_from_group not in all_contacts_after_deletion


