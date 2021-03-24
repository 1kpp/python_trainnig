import re
from random import randrange
from model.contact import Contact


def test_contacts_on_home_page_and_contacts_from_db(app, db):
    # get contacts list from home page
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.max_id)
    # get contacts list from db
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.max_id)
    # compare each object from ui to same object from db
    i = 0
    for item in contacts_from_home_page:
        assert item.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])
        assert item.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
        assert item.address == contacts_from_db[i].address
        assert item.lastname == contacts_from_db[i].lastname.strip()
        assert item.firstname == contacts_from_db[i].firstname.strip()
        i +=1

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