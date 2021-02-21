from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(firstname="NOVbIU KOHTAKT",
                             middlename="NOVbIU KOHTAKT", lastname="NOVbIU KOHTAKT", nickname="NOVbIU KOHTAKT",
                             company="NOVbIU KOHTAKT",
                             zagolovok="NOVbIU KOHTAKT",
                             address="NOVbIU KOHTAKT-Petersburg", home="NOVbIU KOHTAKT", mobile="NOVbIU KOHTAKT",
                             work="NOVbIU KOHTAKT",
                             fax="NOVbIU KOHTAKT", email="NOVbIU KOHTAKT", email2="NOVbIU KOHTAKT",
                             email3="NOVbIU KOHTAKT",
                             homepage="NOVbIU KOHTAKT",
                             bday="25", bmonth="May", byear="1900", aday="1", amonth="May", ayear="2021",
                             address2="NOVbIU KOHTAKT", phone2="NOVbIU KOHTAKT", notes="NOVbIU KOHTAKT"))