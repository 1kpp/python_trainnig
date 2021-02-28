from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name for deletion"))
    old_list = app.contact.get_contact_list()
    index = randrange(len(old_list))
    app.contact.delete_contact_by_index(index)
    new_list = app.contact.get_contact_list()
    assert len(old_list) - 1 == len(new_list)
    old_list[index: index + 1] = []
    assert old_list == new_list

