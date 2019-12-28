# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
import string
import random


# генератор случайных строк
def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # символы в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


testdata = [Contact(last_name="", first_name="", address="")] + [
    Contact(last_name=random_string("first_name", 10), address=random_string("header", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
