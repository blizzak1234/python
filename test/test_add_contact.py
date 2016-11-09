# -*- coding: utf-8 -*-
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(F_name="FN", L_name="LN", C_address="contact_address", C_phone="02", C_email="email@fake.com"))
    app.session.logout()
