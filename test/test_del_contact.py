from model.contact import Contact
from fixture.navigation import NavigationHelper

def test_delete_contact(app):
    if app.contact.is_contacts_exist() == False:
        app.contact.create(Contact(F_name="FN", L_name="LN", C_address="contact_address", C_phone="02", C_email="email@fake.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact()
    app.navigation.return_to_home()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)