# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(first_name="firstname", last_name="last name", address="Moscow", email="test@msk.com",
                mobile="123"))


def test_empty_contact(app):
    app.contact.create(Contact(first_name="", last_name="", address="", email="",
                               mobile=""))