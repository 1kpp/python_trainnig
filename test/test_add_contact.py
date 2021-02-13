# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application


@ pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new_contact(app):
    app.open_home_page()
    app.login( username="admin", password="secret")
    app.create_contact(Contact(firstname="Vladimir",
                   middlename="Ilich", lastname="Ulyanov", nickname="Lenin", company="RSDRP", zagolovok="zagolovok",
                   address="Saint-Petersburg", home="4815162342", mobile="4815162342", work="4815162342",
                   fax="4815162342", email="no email", email2="no email", email3="no email", homepage="no site",
                   bday="22", bmonth="April", byear="1870", aday="22", amonth="April", ayear="2020",
                   address2="Soviet country", phone2="Soviet country", notes="Soviet country"))
    app.return_to_home_page()
    app.logout()
