from selenium.webdriver.support.ui import Select
from model.contact import Contact


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

    def edit(self, contact):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[title='Edit']").click()
        # edit all the fields
        self.fill_form(contact)
        # submit
        wd.find_element_by_css_selector("[value='Update']").click()
        self.return_to_home()
        self.contact_cache = None

    def delete(self):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[title='Edit']").click()
        # click delete
        wd.find_element_by_css_selector("[value='Delete']").click()
        self.return_to_home()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[title='Edit']").click()
        self.fill_form(new_contact_data)
        wd.find_element_by_css_selector("[value='Update']").click()
        self.return_to_home()
        self.contact_cache = None

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
                text_lastname = element.find_element_by_css_selector("tr[name='entry'] > td:nth-child(2)").text
                text_firstname = element.find_element_by_css_selector("tr[name='entry'] > td:nth-child(3)").text
                id = element.find_element_by_css_selector(".center input ").get_attribute("value")
                self.contact_cache.append(Contact(lastname=text_lastname, firstname=text_firstname, id=id))
        return list(self.contact_cache)


