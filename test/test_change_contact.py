from model.contact import Contact
from fixture.navigation import NavigationHelper

def test_change_contact(app):
    if app.contact.is_contacts_exist() == False:
        app.contact.create(Contact(F_name="FN", L_name="LN", C_address="contact_address", C_phone="02", C_email="email@fake.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(F_name="New_name")
    contact.id = old_contacts[0].id
    app.contact.change(contact)
    app.navigation.return_to_home()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
