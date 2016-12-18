from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, Contact):
        # create contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.navigation.return_to_home()
        self.contact_cache = None


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None


    def select_first_contact(self):
        self.select_contact_by_index(0)


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()



    def change(self, new_contact_data):
        # change contact
        self.change_contact_by_index(0)
        self.contact_cache = None


    def change_contact_by_index(self, index, new_contact_data):
        # change contact
        wd = self.app.wd
        self.select_contact_by_index(index)
        # click edit
        wd.find_elements_by_xpath("//form[@name='MainForm']//img[@title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # click update
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        #self.app.navigation.return_to_home()
        self.contact_cache = None


    def fill_contact_form(self, Contact):
        wd = self.app.wd
        # fill group form
        self.app.change_field_value("firstname", Contact.fn)
        self.app.change_field_value("lastname", Contact.ln)
        self.app.change_field_value("address", Contact.c_add)
        self.app.change_field_value("home", Contact.h_phone)
        self.app.change_field_value("mobile", Contact.m_phone)
        self.app.change_field_value("work", Contact.w_phone)
        self.app.change_field_value("phone2", Contact.s_phone)
        self.app.change_field_value("email", Contact.c_email)


    def are_contacts_exist(self):
        wd = self.app.wd
        self.app.navigation.return_to_home()
        if wd.find_element_by_xpath("//div/div[4]/label/strong/span").text == "0":
            return False
        else:
            return True


    def count(self):
        wd = self.app.wd
        self.app.navigation.return_to_home()
        return len(wd.find_elements_by_name("entry"))


    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.return_to_home()
            self.contact_cache = []
            # for element in wd.find_elements_by_name("entry"):
            #     last_name = element.find_element_by_xpath(".//td[2]").text
            #     first_name = element.find_element_by_xpath(".//td[3]").text
            #     id = element.find_element_by_name("selected[]").get_attribute("value")
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails_from_home_page = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(F_name=firstname, L_name=lastname, id=id,
                                                  all_phones_from_home_page = all_phones,
                                                  C_address = address, all_emails_from_home_page = all_emails_from_home_page))

        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(F_name=firstname, L_name=lastname, id=id, H_phone=homephone, W_phone=workphone,
                       M_phone=mobilephone, S_phone=secondaryphone, C_email=email, C_email2=email2, C_email3=email3, C_address=address)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        # ищет по маске "начинается с "Н: " и дальше любые символы до переноса строки. и берет group(1) - это дом. телефон
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(H_phone=homephone, W_phone=workphone,
                       M_phone=mobilephone, S_phone=secondaryphone)



    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None



















