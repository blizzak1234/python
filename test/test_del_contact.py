from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == False:
        app.contact.create(Contact(F_name="FN", L_name="LN", C_address="contact_address", C_phone="02", C_email="email@fake.com"))
    app.contact.delete_contact()
