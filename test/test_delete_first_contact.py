from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="1", middlename="2", lastname="3", nickname="4", title="5", company="6", address="7",home="8", mobile="9", work="10", fax="11", email="12", email2="13", email3="14", homepage="15",bday="1", bmonth="January", byear="2000", aday="3", amonth="July", ayear="2002", address2="16",phone2="17", notes="18"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
