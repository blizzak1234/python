from sys import maxsize


class Contact:

    def __init__(self, F_name=None, L_name=None, C_address=None, C_phone=None, C_email=None, id=None):
        self.fn = F_name
        self.ln = L_name
        self.c_add = C_address
        self.c_phone = C_phone
        self.c_email = C_email
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize