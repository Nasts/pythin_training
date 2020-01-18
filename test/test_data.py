import re
from random import randrange
from fixture.db import DbFixture


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def test_data_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contact_from_home_page))
    contact_from_home_page_by_index = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page_by_index.all_phones_from_home_page == merge_phones_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page_by_index.all_emails_from_home_page == merge_emails_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page_by_index.address == contact_from_edit_page.address

def test_data_db_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()




def clear(s):
    return re.sub("[() \n -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.home_phone, contact.mobile_phone,
                                                           contact.secondary_phone, contact.work_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",[contact.email, contact.second_email, contact.third_email]))