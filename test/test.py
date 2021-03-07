from selenium import webdriver

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, zagolovok=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None,
                 phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.zagolovok = zagolovok
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

wd = webdriver.Firefox()
wd.implicitly_wait(0.5)
wd.get("http://localhost/addressbook/")
contacts = []
for element in wd.find_elements_by_name("entry"):
    text_lastname = element.find_element_by_xpath("//child::td[2]").text
    text_firstname = element.find_element_by_xpath("//child::td[3]").text
    id = element.find_element_by_css_selector(".center input ").get_attribute("value")
    contacts.append(Contact(lastname=text_lastname, firstname=text_firstname, id=id))
print(contacts)