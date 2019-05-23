# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1", middlename="2", lastname="3", nickname="4", title="5", company="6", address="7", home="8", mobile="9", work="10", fax="11", email="12", email2="13", email3="14", homepage="15",
                               bday="1", bmonth="January", byear="2000", aday="3", amonth="July", ayear="2002", address2="16", phone2="17", notes="18")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
