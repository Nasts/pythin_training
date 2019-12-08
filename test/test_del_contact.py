# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="firstname", last_name="last name", address="Moscow", email="test@msk.com",
                mobile="123"))
    app.contact.delete_first_contact()