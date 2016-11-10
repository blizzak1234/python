from model.contact import Contact

def test_change_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.change(Contact(F_name="FN_ch", L_name="LN_ch", C_address="contact_address_ch", C_phone="02_1", C_email="email_ch@fake.com"))
    app.session.logout()