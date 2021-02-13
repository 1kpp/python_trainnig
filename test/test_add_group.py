# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application_group import Application
import pytest

@ pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login( username="admin", password="secret")
    app.create_group( Group(name="asdsad", header="13123123", footer="asdsadd"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()