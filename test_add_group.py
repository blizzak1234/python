# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def open_home_page(self, wd):
    # open home page
    wd.get("http://localhost/addressbook/")


def login(self, wd, username, password):
    # login
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


def open_groups_page(self, wd):
    # open groups page
    wd.find_element_by_link_text("groups").click()


def create_group(self, wd, name, header, footer):
    # init group creation
    wd.find_element_by_name("new").click()
    # fill group form
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys(name)
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys(header)
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys(footer)
    # submit group creation
    wd.find_element_by_name("submit").click()


def return_to_groups_page(self, wd):
    # return groups page
    wd.find_element_by_link_text("groups").click()


def logout(self, wd):
    # logout
    wd.find_element_by_link_text("Logout").click()

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(firefox_binary=FirefoxBinary("C:\\Program Files\\FF_ESR\\firefox.exe"))
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, name="group_name", header="group_logo", footer="group_comment")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, name="", header="", footer="")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
