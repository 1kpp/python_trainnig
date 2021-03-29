from selenium.webdriver.support.ui import Select
from model.contact import Contact
from fixture.orm import ORMFixture
import random
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # filling the form
        self.fill_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home()
        self.contact_cache = None

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        self.select_contact_by_index(index)
        # edit all the fields
        self.fill_form(contact)
        # submit
        wd.find_element_by_css_selector("[value='Update']").click()
        self.return_to_home()
        self.contact_cache = None

    def edit_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        self.select_contact_by_id(id)
        # edit all the fields
        self.fill_form(contact)
        # submit
        wd.find_element_by_css_selector("[value='Update']").click()
        self.return_to_home()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        self.select_contact_by_index(index)
        # click delete
        wd.find_element_by_css_selector("[value='Delete']").click()
        self.return_to_home()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        self.select_contact_by_id(id)
        # click delete
        wd.find_element_by_css_selector("[value='Delete']").click()
        self.return_to_home()
        self.contact_cache = None

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        self.select_contact_by_index(index)
        self.fill_form(new_contact_data)
        wd.find_element_by_css_selector("[value='Update']").click()
        self.return_to_home()
        self.contact_cache = None

    def modify_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        self.select_contact_by_id(id)
        self.fill_form(new_contact_data)
        wd.find_element_by_css_selector("[value='Update']").click()
        self.return_to_home()
        self.contact_cache = None

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_checkbox(contact_id)
        self.select_random_group_from_list(group_id)
        self.return_to_home()
        self.contact_cache = None

    def select_random_group_from_list(self, group_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("select[name='to_group'] [value='%s']" %group_id).click()
        wd.find_element_by_css_selector("[name='add']").click()

    def delete_contact_from_group(self, group_with_contact_id):
        wd = self.app.wd
        self.return_to_home()
        wd.find_element_by_css_selector("select[name='group'] option[value='%s']" % group_with_contact_id).click()
        wd.find_element_by_css_selector("td[class='center'] input[type='checkbox']").click()
        wd.find_element_by_name("remove").click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home()
        wd.find_element_by_css_selector("input[value='%s']" %id).click()
        # wd.find_element_by_partial_link_text(("%s") %id).click()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        # wd.find_element_by_css_selector("[title='Edit']")[index].click()

    def select_contact_checkbox(self, contact_id):
        wd = self.app.wd
        self.return_to_home()
        wd.find_element_by_id("%s" %contact_id).click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_css_selector("[title='Edit']")[index].click()

    def select_contact_by_index_to_view(self, index):
        wd = self.app.wd
        self.return_to_home()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_css_selector("[title='Details']")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[title='Edit']").click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def return_to_home(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_date(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("title", contact.zagolovok)
        self.type("company", contact.company)
        self.type("address", contact.address)
        self.type("home", contact.home)
        self.type("mobile", contact.mobile)
        self.type("work", contact.work)
        self.type("fax", contact.fax)
        self.type("email", contact.email)
        self.type("email2", contact.email2)
        self.type("email3", contact.email3)
        self.type("homepage", contact.homepage)
        self.select_date("bday", contact.bday)
        self.select_date("bmonth", contact.bmonth)
        self.type("byear", contact.byear)
        self.select_date("aday", contact.aday)
        self.select_date("amonth", contact.amonth)
        self.type("ayear", contact.ayear)
        self.type("address2", contact.address2)
        self.type("phone2", contact.phone2)
        self.type("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                text_lastname = cells[1].text
                text_firstname = cells[2].text
                id = element.find_element_by_css_selector(".center input ").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(lastname=text_lastname, firstname=text_firstname, id=id,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones,
                                                  address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, home=homephone,
                       mobile=mobilephone, work=workphone, phone2=phone2, id=id,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_list_from_view_page(self, index):
        wd = self.app.wd
        self.select_contact_by_index_to_view(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone,
                       mobile= mobilephone, work= workphone, phone2=phone2)

