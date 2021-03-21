from model.contact import Contact
import random


def test_edit_contact(app,db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="name for edition"))
    old_list = db.get_contact_list()
    random_contact = random.choice(old_list)
    index = old_list.index(random_contact)
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
    app.contact.edit_contact_by_id(contact, random_contact.id)
    new_list = db.get_contact_list()
    assert len(old_list) == len(new_list)
    old_list[index] = contact
    assert old_list == new_list
    if check_ui:
        assert sorted(new_list, key=Contact.max_id) == sorted(app.contact.get_contact_list(), key=Contact.max_id)


