from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def go_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_partial_link_text("group page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("mobile_phone", contact.mobile_phone)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # init edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit edit
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog window
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def add_contact_by_index_to_group(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # init add to group
        wd.find_element_by_name("add").click()
        self.go_to_group_page()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('addressbook/') and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    contact_cache = None

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.return_to_home_page()
    #         self.contact_cache = []
    #         count = len(wd.find_elements_by_xpath('//*[@id="maintable"]/tbody/tr'))
    #         for i in range(2, count + 1):
    #             object_last_name = wd.find_elements_by_xpath(f'//*[@id="maintable"]/tbody/tr[{i}]/td[2]')
    #             text_last_name = object_last_name[0].text
    #             id = wd.find_elements_by_xpath(f'//*[@id="maintable"]/tbody/tr[{i}]/td[1]/input')[0].get_attribute(
    #                 'value')
    #             object_first_name = wd.find_elements_by_xpath(f'//*[@id="maintable"]/tbody/tr[{i}]/td[3]')
    #             text_first_name = object_first_name[0].text
    #             self.contact_cache.append(Contact(last_name=text_last_name, first_name=text_first_name, id=id))
    #     return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(last_name=last_name, first_name=first_name, id=id, all_phones_from_home_page=all_phones,
                            all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        second_email = wd.find_element_by_name("email2").get_attribute("value")
        third_email = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        return Contact(last_name=last_name, first_name=first_name, id=id, address=address, email=email, second_email=second_email,
                       third_email=third_email, mobile_phone=mobile_phone,
                       home_phone=home_phone, secondary_phone=secondary_phone, work_phone=work_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(mobile_phone=mobile_phone,
                       home_phone=home_phone, secondary_phone=secondary_phone, work_phone=work_phone)
