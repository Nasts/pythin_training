# -*- coding: utf-8 -*-
import random
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
from model.contact import Contact


def test_add_some_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="firstname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    group_list = app.group.get_group_list()
    for group in group_list:
        contacts_not_in_group = db.get_contacts_not_in_group(group)
        if not contacts_not_in_group:
            app.contact.create(Contact(first_name="firstname"))
        else:
            contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_by_id_to_group(contact, group)
    contact_list = db.get_contacts_in_group(group)
    assert contact in contact_list
