# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app, json_contacts):
    contact = json_contacts
    old_list = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_list) + 1 == app.contact.count()
    new_list = app.contact.get_contact_list()
    old_list.append(contact)
    assert sorted(new_list, key=Contact.max_id) == sorted(old_list, key=Contact.max_id)

