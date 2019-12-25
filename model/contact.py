from sys import maxsize


class Contact:

    def __init__(self, last_name=None, first_name=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None, address=None,
                 email=None, second_email=None, third_email=None, mobile_phone=None, home_phone=None,
                 secondary_phone=None, work_phone=None):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.email = email
        self.second_email = second_email
        self.third_email = third_email
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.secondary_phone = secondary_phone
        self.work_phone = work_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.first_name,)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
