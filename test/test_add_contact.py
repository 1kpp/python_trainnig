# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_list = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_list) + 1 == app.contact.count()
    new_list = db.get_contact_list()
    old_list.append(contact)
    assert sorted(new_list, key=Contact.max_id) == sorted(old_list, key=Contact.max_id)
    if check_ui:
        assert sorted(new_list, key=Contact.max_id) == sorted(app.contact.get_contact_list(), key=Contact.max_id)

