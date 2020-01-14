# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_add_some_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="firstname"))
    old_list_contacts = db.get_contact_list()
    contact = random.choice(old_list_contacts)
    app.contact.add_contact_by_id_to_group(contact.id)
    new_list_contacts = db.get_contact_list()
    assert old_list_contacts == new_list_contacts