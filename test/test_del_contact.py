from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name for deletion"))
    old_list = app.contact.get_contact_list()
    app.contact.delete()
    new_list = app.contact.get_contact_list()
    assert len(old_list) - 1 == len(new_list)
    old_list[0:1] = []
    assert old_list == new_list

