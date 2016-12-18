# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    #old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    # contact = Contact(F_name="FN", L_name="LN", C_address="contact_address", H_phone="02", M_phone="5456",
    #                   W_phone="6543", S_phone="76543", C_email="email@fake.com")
    app.contact.create(contact)
    #assert len(old_contacts) + 1 == app.contact.count() #хеширование
    #new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)