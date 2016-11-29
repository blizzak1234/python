from sys import maxsize


class Contact:

    def __init__(self, F_name=None, L_name=None, C_address=None, H_phone=None, W_phone=None, M_phone=None, S_phone=None, C_email=None, id=None):
        self.fn = F_name
        self.ln = L_name
        self.c_add = C_address
        self.h_phone = H_phone
        self.w_phone = W_phone
        self.m_phone = M_phone
        self.s_phone = S_phone
        self.c_email = C_email
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


    def __repr__(self):
        return "%s, %s, %s" % (self.id, self.fn, self.ln)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.fn == other.fn