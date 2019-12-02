# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(
        Contact(first_name="edit_first_name", last_name="edit_last_name", address="edit_Moscow", email="edit_test@msk.com",
                mobile="edit_123"))
    app.session.logout()
