# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    contact = Contact(first_name="edit_first_name_4", last_name="edit_last_name_4")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    edit_contact = random.choice(old_contacts)
    contact.id = edit_contact.id
    app.contact.edit_contact_by_id(edit_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[old_contacts.index(edit_contact)] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_edit_address_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="edit_first_name", last_name="edit_last_name"))
#     app.contact.edit_contact(Contact(address="Krasnodar"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
