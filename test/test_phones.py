

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.h_phone == contact_from_edit_page.h_phone
    assert contact_from_home_page.w_phone == contact_from_edit_page.w_phone
    assert contact_from_home_page.m_phone == contact_from_edit_page.m_phone
    assert contact_from_home_page.s_phone == contact_from_edit_page.s_phone