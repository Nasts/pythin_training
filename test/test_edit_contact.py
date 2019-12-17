# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_edit_contact(app):
    contact = Contact(first_name="edit_first_name", last_name="edit_last_name")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_address_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="edit_first_name", last_name="edit_last_name"))
#     app.contact.edit_contact(Contact(address="Krasnodar"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
