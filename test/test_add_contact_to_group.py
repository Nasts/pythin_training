# -*- coding: utf-8 -*-
import random
from sys import maxsize

from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_some_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="firstname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    group_list = db.get_group_list()
    contact_list = db.get_contact_list()
    contact = None
    group = None
    for g in group_list:
        list_contacts_not_in_group = db.get_contacts_not_in_group(g)
        if list_contacts_not_in_group:
            contact = random.choice(list_contacts_not_in_group)
            app.contact.add_contact_by_id_to_group(contact, g)
            group = g
            break
    if contact is None:
        header = 'testedition'
        app.group.create(Group(header=header))
        group = db.get_group_by_header(header)
        contact = random.choice(contact_list)
        app.contact.add_contact_by_id_to_group(contact, group)

    contacts = db.get_contacts_in_group(group)
    assert contact in contacts




    # for group in group_list:
    #     list_contacts_not_in_group = db.get_contacts_not_in_group(group)
    #     if list_contacts_not_in_group:
    #         contact = random.choice(list_contacts_not_in_group)
    #         app.contact.add_contact_by_id_to_group(contact, group)
    #         break
    #     else:
    #         contact = Contact(id = maxsize, first_name="edit_first_name_4", last_name="edit_last_name_4")
    #         group = random.choice(group_list)
    #         app.contact.add_contact_by_id_to_group(contact, group)
    #         break
    # contact_list = db.get_contacts_in_group(group)
    # assert contact in contact_list
