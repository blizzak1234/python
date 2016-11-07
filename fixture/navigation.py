

class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def return_to_home(self):
        # return to home page
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
