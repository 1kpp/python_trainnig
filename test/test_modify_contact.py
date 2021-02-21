from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Old name", middlename="Old middlename", bday="25", notes="Ol notes"))
    app.contact.modify_first_contact(Contact(firstname="New name", middlename="New middlename", bday="25", notes="New notes"))