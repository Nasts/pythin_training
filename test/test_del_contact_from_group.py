# -*- coding: utf-8 -*-
import random
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_some_contact_from_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="firstname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    if len(db.get_contacts_in_any_groups()) == 0:
        group = random.choice(app.group.get_group_list())
        contact = random.choice(app.contact.get_contact_list())
        app.contact.add_contact_by_id_to_group(contact, group)
    group_list = app.group.get_group_list()
    for item in group_list:
        contacts_in_group = db.get_contacts_in_group(item)
        if contacts_in_group:
            contact = random.choice(contacts_in_group)
            app.contact.remove_contact_by_id_to_group(contact, item)
            contact_list = db.get_contacts_in_group(item)
            assert contact not in contact_list
            break


