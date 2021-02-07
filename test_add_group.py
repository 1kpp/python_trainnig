# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_section(wd)
        self.create_group(wd, group_name="asdsad", header="13123123", footer="asdsadd")
        self.return_to_groups(wd)
        self.lodout(wd)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_section(wd)
        self.create_group(wd, group_name="", header="", footer="")
        self.return_to_groups(wd)
        self.lodout(wd)


    def lodout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group_name, header, footer):
        # Create a new group
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()

    def open_group_section(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        # Log in
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
