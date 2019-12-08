class ContactHelper:

    def __init__(self, app):
        self.app = app

    def go_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_partial_link_text("group page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("mobile", contact.mobile)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()

    def edit_contact(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # init edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit edit
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog window
        wd.switch_to_alert().accept()

    def add_first_contact_to_group(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # init add to group
        wd.find_element_by_name("add").click()
        self.go_to_group_page()
