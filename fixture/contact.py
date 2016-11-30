from model.contact import Contact
from fixture.navigation import NavigationHelper

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


    def change(self, new_contact_data):
        # change contact
        self.change_contact_by_index(0)
        self.contact_cache = None


    def change_contact_by_index(self, index, new_contact_data):
        # change contact
        wd = self.app.wd
        self.select_contact_by_index(index)
        # click edit
        #tmp_index = str(index+1)
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + tmp_index + "]/td[8]/a/img").click()
        # for row in wd.find_elements_by_name("entry"):
        #     cells = row.find_elements_by_tag_name("td")
        #     firstname = cells[2].text
        #     lastname = cells[1].text
        #     id = cells[0].find_element_by_tag_name("input").get_attribute("value")
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
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(F_name=firstname, L_name=lastname, id=id, H_phone=all_phones[0],
                                                  M_phone=all_phones[1], W_phone=all_phones[2], S_phone=all_phones[3]))
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
        return Contact(F_name=firstname, L_name=lastname,id=id, H_phone=homephone, W_phone=workphone,
                       M_phone=mobilephone, S_phone=secondaryphone)


























