# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="1", middlename="2", lastname="3", nickname="4", title="5", company="6", address="7", home="8", mobile="9", work="10", fax="11", email="12", email2="13", email3="14", homepage="15",
                            bday="1", bmonth="January", byear="2000", aday="3", amonth="July", ayear="2002", address2="16", phone2="17", notes="18"))
    app.session.logout()
