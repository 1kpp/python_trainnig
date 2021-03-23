from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, check_ui):
    # checks whether there are contacts available. If not - create one
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="Name for deletion"))
    # check whether there are groups available. If not - create one
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="azazazaz"))
    list_of_contacts = db.get_contact_list()
    # choose random contact to add
    random_contact = random.choice(list_of_contacts)
    # choose random group for contact addition
    random_group = random.choice(db.get_group_list())
    # add contact to group
    app.contact.add_contact_to_group(random_contact.id, random_group.id)
    assert db.get_contact_in_group(random_group, random_contact) == random_contact
