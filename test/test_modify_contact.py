from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="Old name", middlename="Old middlename", bday="25", notes="Ol notes"))
    old_list = db.get_contact_list()
    random_contact = random.choice(old_list)
    index = old_list.index(random_contact)
    contact = Contact(firstname="New name", middlename="New middlename", bday="25", notes="New notes")
    app.contact.modify_contact_by_id(contact, random_contact.id)
    new_list = db.get_contact_list()
    assert len(old_list) == len(new_list)
    old_list[index] = contact
    assert old_list == new_list
    if check_ui:
        assert sorted(new_list, key=Contact.max_id) == sorted(app.contact.get_contact_list(), key=Contact.max_id)


