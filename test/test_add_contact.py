# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

#случайные строки для имени
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайные строки для имейла
def random_string_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "." + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайные строки для телефона
def random_string_phone(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайные строки для адреса
def random_string_add(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(F_name=random_string("fn", 5), L_name=random_string("ln", 5),
                    C_address=random_string_add("addr", 5),H_phone=random_string_phone("home_", 7),
                    M_phone=random_string_phone("mobile_", 10), W_phone=random_string_phone("work_", 8),
                    S_phone=random_string_phone("sec_", 9), C_email=random_string_email("email_", 4))]





@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(F_name="FN", L_name="LN", C_address="contact_address", H_phone="02", M_phone="5456",
    #                   W_phone="6543", S_phone="76543", C_email="email@fake.com")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

