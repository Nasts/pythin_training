# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


# def test_add_first_contact_to_group(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="firstname"))
#     app.contact.add_first_contact_to_group()


def test_add_some_contact_to_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="firstname"))
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    app.contact.add_contact_by_index_to_group(index)