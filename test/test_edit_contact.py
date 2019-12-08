# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="edit_first_name", last_name="edit_last_name"))
    app.contact.edit_contact(
        Contact(first_name="edit_first_name", last_name="edit_last_name", address="edit_Moscow",
                email="edit_test@msk.com",
                mobile="edit_123"))


def test_edit_address_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="edit_first_name", last_name="edit_last_name"))
    app.contact.edit_contact(Contact(address="Krasnodar"))
