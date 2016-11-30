from model.contact import Contact
from random import randrange
from sys import maxsize

def test_change_contact(app):
    if app.contact.are_contacts_exist() == False:
        app.contact.create(Contact(F_name="FN", L_name="LN", C_address="contact_address", H_phone="02",
                                   C_email="email@fake.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(F_name="New_name", L_name="New_LN")
    contact.id = old_contacts[index].id #запоминает айди модифицируемого контакта.
    app.contact.change_contact_by_index(index, contact)
    #app.navigation.return_to_home()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact # заменяет выбранный на редактирование контакт новым контактом
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
