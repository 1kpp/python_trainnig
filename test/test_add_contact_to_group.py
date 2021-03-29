from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, check_ui):
    # checks whether there are contacts available. If not - create one
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Name for deletion"))
    # check whether there are groups available. If not - create one
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="azazazaz"))
    # check whether there are free contacts (not part of any group)
    if len(db.get_contacts_not_in_any_of_groups()) == 0:
        app.contact.create(Contact(firstname="Contact not in groups"))
    # check whether there are free groups (do not have any contacts inside)
    if len(db.get_groups_without_contacts()) == 0:
        app.group.create(Group(name="Group without contacts"))
    # choose random contact to add
    random_contact = random.choice(db.get_contacts_not_in_any_of_groups())
    # choose random group for contact addition
    random_group = random.choice(db.get_groups_without_contacts())
    # add contact to group
    app.contact.add_contact_to_group(random_contact.id, random_group.id)
    # assert that random_contact is in list of contacts of random_group
    assert random_contact in db.get_contact_in_group(random_group)
