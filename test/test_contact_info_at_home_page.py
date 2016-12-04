from model.contact import Contact
import re
from random import randrange

def test_data_at_home_page(app):
    if app.contact.are_contacts_exist() == False:
        app.contact.create(Contact(F_name="FN", L_name="LN", C_address="contact_address", H_phone="02",
                                   C_email="email@fake.com"))
    # выбрать контакт
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))
    memory_index = index
    # получить список его полей
    contact_from_home_page = app.contact.get_contact_list()[index]
    # открыть контакт на редактирование
    # получить список полей
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # сравнить FN
    assert contact_from_home_page.fn == contact_from_edit_page.fn
    # сравнить LN
    assert contact_from_home_page.ln == contact_from_edit_page.ln
    # сравнить адрес
    assert contact_from_home_page.c_add == contact_from_edit_page.c_add
    # сравнить имейлы
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    # сравнить телефоны
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


#очищает строки от лишних символов. тк мы сравниваем 2 страницы и на одной номера с символами, на другой без
def clear_phones(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    #на входе полная строка.  join - все склеивает
    return "\n".join(filter (lambda x: x != "", #filter - прореживает удаляя пустые строки.
                             map(lambda x: clear_phones(x), #map - очищает через clear.
                                 filter(lambda x: x is not None, #отфильтровывает все значения None
                                        [contact.h_phone, contact.m_phone, contact.w_phone, contact.s_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join([contact.c_email, contact.c_email2, contact.c_email3])