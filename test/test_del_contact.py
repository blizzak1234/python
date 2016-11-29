from model.contact import Contact
from random import randrange

def test_delete_contact(app):
    if app.contact.are_contacts_exist() == False:
        app.contact.create(Contact(F_name="FN", L_name="LN", C_address="contact_address", H_phone="02", C_email="email@fake.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

