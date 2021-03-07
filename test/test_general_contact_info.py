import re
from random import randrange


def test_contact_info_on_home_page(app):
    list_of_contacts = app.contact.get_contact_list()
    index = randrange(len(list_of_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


# def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_list_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert clear(contact_from_view_page.home) == clear(contact_from_edit_page.home)
#    assert clear(contact_from_view_page.mobile) == clear(contact_from_edit_page.mobile)
#    assert clear(contact_from_view_page.work) == clear(contact_from_edit_page.work)
#    assert clear(contact_from_view_page.phone2) == clear(contact_from_edit_page.phone2)


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