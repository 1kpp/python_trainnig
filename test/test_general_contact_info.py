import re
from random import randrange
from model.contact import Contact


# def test_contact_info_on_home_page(app):
#     list_of_contacts = app.contact.get_contact_list()
#     index = randrange(len(list_of_contacts))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname


def test_contacts_on_home_page_and_contacts_from_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert sorted(contacts_from_db, key=Contact.max_id) == sorted(contacts_from_home_page, key=Contact.max_id)
    # assert contacts_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db)
    # assert contacts_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db)
    # assert contacts_from_home_page.address == contacts_from_db.address
    # assert contacts_from_home_page.lastname == contacts_from_db.lastname
    # assert contacts_from_home_page.firstname == contacts_from_db.firstname


def clear(s):
    return re.sub("[() -+]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3])))