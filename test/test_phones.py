import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.w_phone == clear(contact_from_edit_page.w_phone)
    # assert contact_from_home_page.m_phone == clear(contact_from_edit_page.m_phone)
    # assert contact_from_home_page.s_phone == clear(contact_from_edit_page.s_phone)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.h_phone == contact_from_edit_page.h_phone
    assert contact_from_view_page.w_phone == contact_from_edit_page.w_phone
    assert contact_from_view_page.m_phone == contact_from_edit_page.m_phone
    assert contact_from_view_page.s_phone == contact_from_edit_page.s_phone

#очищает строки от лишних символов. тк мы сравниваем 2 страницы и на одной номера с символами, на другой без
def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    #на входе полная строка.  join - все склеивает
    return "\n".join(filter (lambda x: x != "", #filter - прореживает удаляя пустые строки.
                             map(lambda x: clear(x), #map - очищает через clear.
                                 filter(lambda x: x is not None, #отфильтровывает все значения None
                                        [contact.h_phone, contact.m_phone, contact.w_phone, contact.s_phone]))))