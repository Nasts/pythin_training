# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_del_some_contact(app, db):
    old_contacts = db.get_contact_list()
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(first_name="firstname", last_name="last name", address="Moscow", email="test@msk.com",
                    mobile="123"))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
