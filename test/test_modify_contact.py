from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Old name", middlename="Old middlename", bday="25", notes="Ol notes"))
    old_list = app.contact.get_contact_list()
    contact = Contact(firstname="New name", middlename="New middlename", bday="25", notes="New notes")
    contact.id = old_list[0].id
    app.contact.modify_first_contact(contact)
    new_list = app.contact.get_contact_list()
    assert len(old_list) == len(new_list)
    old_list[0] = contact
    assert sorted(old_list, key=Contact.max_id) == sorted(new_list, key=Contact.max_id)