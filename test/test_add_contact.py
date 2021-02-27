# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_list = app.contact.get_contact_list()
    contact = Contact(firstname="NAME",
                               middlename="SECOND NAME", lastname="SURNAME", nickname="Lenin", company="RSDRP", zagolovok="zagolovok",
                               address="Saint-Petersburg", home="4815162342", mobile="4815162342", work="4815162342",
                               fax="4815162342", email="no email", email2="no email", email3="no email", homepage="no site",
                               bday="22", bmonth="April", byear="1870", aday="22", amonth="April", ayear="2020",
                               address2="Soviet country", phone2="Soviet country", notes="Soviet country")
    app.contact.create(contact)
    new_list = app.contact.get_contact_list()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(contact)
    assert sorted(new_list, key=Contact.max_id) == sorted(old_list, key=Contact.max_id)

