from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="name for edition"))
    old_list = app.contact.get_contact_list()
    index = randrange(len(old_list))
    contact = Contact(firstname="NOVbIU KOHTAKT",
                             middlename="NOVbIU KOHTAKT", lastname="NOVbIU KOHTAKT", nickname="NOVbIU KOHTAKT",
                             company="NOVbIU KOHTAKT",
                             zagolovok="NOVbIU KOHTAKT",
                             address="NOVbIU KOHTAKT-Petersburg", home="NOVbIU KOHTAKT", mobile="NOVbIU KOHTAKT",
                             work="NOVbIU KOHTAKT",
                             fax="NOVbIU KOHTAKT", email="NOVbIU KOHTAKT", email2="NOVbIU KOHTAKT",
                             email3="NOVbIU KOHTAKT",
                             homepage="NOVbIU KOHTAKT",
                             bday="25", bmonth="May", byear="1900", aday="1", amonth="May", ayear="2021",
                             address2="NOVbIU KOHTAKT", phone2="NOVbIU KOHTAKT", notes="NOVbIU KOHTAKT")
    contact.id = old_list[index].id
    app.contact.edit_contact_by_index(contact, index)
    new_list = app.contact.get_contact_list()
    assert len(old_list) == len(new_list)
    old_list[index] = contact
    assert sorted(old_list, key=Contact.max_id) == sorted(new_list, key=Contact.max_id)