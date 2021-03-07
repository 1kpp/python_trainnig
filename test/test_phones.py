import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_home_page.home) == clear(contact_from_edit_page.home)
    assert clear(contact_from_home_page.mobile) == clear(contact_from_edit_page.mobile)
    assert clear(contact_from_home_page.work) == clear(contact_from_edit_page.work)
    assert clear(contact_from_home_page.phone2) == clear(contact_from_edit_page.phone2)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_list_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_view_page.home) == clear(contact_from_edit_page.home)
    assert clear(contact_from_view_page.mobile) == clear(contact_from_edit_page.mobile)
    assert clear(contact_from_view_page.work) == clear(contact_from_edit_page.work)
    assert clear(contact_from_view_page.phone2) == clear(contact_from_edit_page.phone2)


def clear(s):
    return re.sub("[() -+]", "", s)