from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # wd.find_element_by_name("group_name").click()
        # wd.find_element_by_name("group_name").clear()
        # wd.find_element_by_name("group_name").send_keys(group.name)
        # wd.find_element_by_name("group_header").click()
        # wd.find_element_by_name("group_header").clear()
        # wd.find_element_by_name("group_header").send_keys(group.header)
        # wd.find_element_by_name("group_footer").click()
        # wd.find_element_by_name("group_footer").clear()
        # wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        # return groups page
        wd.find_element_by_link_text("groups").click()


   # def change(self, group):
    #    wd = self.app.wd
     #   self.open_groups_page()
      #  self.select_first_group()
       # # init group modification
       # wd.find_element_by_name("edit").click()
       # self.fill_group_form(group)
        # submit group creation
        #wd.find_element_by_name("update").click()
        #self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        # fill group form
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
            return list(self.group_cache) #возвращаем кэш. Лист для того чтобы кэш был неизменным. Если его испортили снаружи

































