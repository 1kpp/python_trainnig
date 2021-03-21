from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="Name for deletion"))
    old_list = db.get_contact_list()
    contact = random.choice(old_list)
    app.contact.delete_contact_by_id(contact.id)
    new_list = db.get_contact_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(contact)
    assert old_list == new_list
    if check_ui:
        assert sorted(new_list, key=Contact.max_id) == sorted(app.contact.get_contact_list(), key=Contact.max_id)



