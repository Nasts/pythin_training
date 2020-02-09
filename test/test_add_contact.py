# -*- coding: utf-8 -*-
import allure
import pytest

from model.contact import Contact


@pytest.mark.skip(reason="Skipped Test")
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("When I add a contact to the list"):
        app.contact.create(contact)
    with allure.step("Then the new contact list is equal to the old list with the added group"):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)
