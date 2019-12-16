# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="firstname", last_name="last name", address="Moscow", email="test@msk.com",
                mobile="123"))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) -1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts