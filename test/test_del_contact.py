# -*- coding: utf-8 -*-
import random

import allure

from model.contact import Contact


def test_del_some_contact(app, db):
    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
        if len(db.get_contact_list()) == 0:
            app.contact.create(
                Contact(first_name="firstname", last_name="last name", address="Moscow", email="test@msk.com",
                        mobile="123"))
    with allure.step("When I choice a contact from the list"):
        contact = random.choice(old_contacts)
    with allure.step("Then I delete a contact by id"):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step("Then the new contact list is equal to the old list without the deleted contact"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
