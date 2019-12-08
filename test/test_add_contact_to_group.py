# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_first_contact_to_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="firstname"))
    app.contact.add_first_contact_to_group()
