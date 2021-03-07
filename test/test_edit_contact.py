from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="name for edition"))
    old_list = app.contact.get_contact_list()
    index = randrange(len(old_list))
    contact = Contact(firstname="NOVbIU KOHTAKT",
                             middlename="middlename", lastname="lastname", nickname="nickname",
                             company="company",
                             zagolovok="zagolovok",
                             address="NOVbIU KOHTAKT-Petersburg", home="0123", mobile="0123",
                             work="0123",
                             fax="0123", email="654126845", email2="email2",
                             email3="NOVbIU KOHTAKT",
                             homepage="homepage",
                             bday="25", bmonth="May", byear="1900", aday="1", amonth="May", ayear="2021",
                             address2="address2", phone2="685312564", notes="notes")
    contact.id = old_list[index].id
    app.contact.edit_contact_by_index(contact, index)
    new_list = app.contact.get_contact_list()
    assert len(old_list) == len(new_list)
    old_list[index] = contact
    assert sorted(old_list, key=Contact.max_id) == sorted(new_list, key=Contact.max_id)