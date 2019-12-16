from sys import maxsize


class Contact:

    def __init__(self, first_name=None, last_name=None, address=None, email=None, mobile=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.mobile = mobile
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
