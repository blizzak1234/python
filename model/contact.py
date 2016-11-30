from sys import maxsize


class Contact:

    def __init__(self, F_name=None, L_name=None, C_address=None, all_phones_from_home_page=None,
                 H_phone=None, W_phone=None, M_phone=None, S_phone=None, C_email=None, id=None):
        self.fn = F_name
        self.ln = L_name
        self.c_add = C_address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.h_phone = H_phone
        self.w_phone = W_phone
        self.m_phone = M_phone
        self.s_phone = S_phone
        self.c_email = C_email
        self.id = id



    # representation. стандартная функция, позволяющая определить как выглядит объект при выводе на консоль. для того, чтобы было понятно что в ошибках сравнения.
    def __repr__(self):
        return "%s, %s, %s" % (self.id, self.fn, self.ln)

    # equals. стандартная функция, которая принимает в качестве второго параметра объект, с которым нужно сравнить объект self. Чтобы сравнивались объекты без учета того где они лежат в памяти.
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.ln == other.ln and self.fn == other.fn

    # вычисляет айди контакта по контакту. если айди есть - возвращает айди, если айди нет - возвращает максимальное целое число.
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
