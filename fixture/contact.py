from model.contact import Contact

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


    def delete_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        # select contact
        wd.find_element_by_name("selected[]").click()

    def change(self, new_contact_data):
        # change contact
        wd = self.app.wd
        self.select_first_contact()
        # click edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # click update
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        #self.app.navigation.return_to_home()

    def fill_contact_form(self, Contact):
        wd = self.app.wd
        # fill group form
        self.app.change_field_value("firstname", Contact.fn)
        self.app.change_field_value("lastname", Contact.ln)
        self.app.change_field_value("address", Contact.c_add)
        self.app.change_field_value("home", Contact.c_phone)
        self.app.change_field_value("email", Contact.c_email)


    def count(self):
        wd = self.app.wd
        if wd.find_element_by_xpath("//div/div[4]/label/strong/span").text == "0":
            return False
        else:
            return True


    def get_contact_list(self):
        wd = self.app.wd
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            last_name = element.find_element_by_xpath(".//td[2]").text
            first_name = element.find_element_by_xpath(".//td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(F_name=first_name, L_name=last_name, id=id))
        return contacts
