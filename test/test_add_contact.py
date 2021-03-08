# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testData = [Contact(firstname="", middlename="", lastname="", nickname="", company="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 15), company=random_string("company", 15))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testData, ids=[repr(x) for x in testData])
def test_add_new_contact(app, contact):
    old_list = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_list) + 1 == app.contact.count()
    new_list = app.contact.get_contact_list()
    old_list.append(contact)
    assert sorted(new_list, key=Contact.max_id) == sorted(old_list, key=Contact.max_id)

