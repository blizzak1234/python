from model.contact import Contact
import random


def test_change_contact(app, db, check_ui):
    if app.contact.are_contacts_exist() == False:
        app.contact.create(Contact(F_name="FN", L_name="LN", C_address="contact_address", H_phone="02",
                                   C_email="email@fake.com"))
    #old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_info = Contact(F_name="New_name", L_name="New_LN")
    contact_info.id = contact.id
    #contact.id = old_contacts[index].id #запоминает айди модифицируемого контакта.
    app.contact.change_contact_by_id(contact.id, contact_info)
    #app.navigation.return_to_home()
    #assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    #old_contacts[id] = contact # заменяет выбранный на редактирование контакт новым контактом
    old_contacts.remove(contact)
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # if check_ui:
    #     assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
