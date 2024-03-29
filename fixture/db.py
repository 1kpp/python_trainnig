import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from model.contacts_groups_link import ContactsGroups
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, email, email2, email3, address, address2, home,"
                           "mobile, work, fax, phone2 from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, email, email2, email3, address, address2, home,
                    mobile, work, fax, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, address=address,
                                    home=home,mobile=mobile, work= work,  fax=fax, email=email, email2=email2, email3=email3, address2=address2,
                                    phone2=phone2))
        finally:
            cursor.close()
        return list

    def get_contacts_groups_table(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(ContactsGroups(id=id, group_id=group_id))
        finally:
            cursor.close()
        return list

    def get_contact_in_group(self, random_group):
        return db.get_contacts_in_group(random_group)

    def get_contacts_not_in_any_of_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname FROM addressbook where id not in (SELECT id from address_in_groups)")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_groups_without_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name FROM group_list where group_id not in "
                           "(SELECT group_id from address_in_groups)")
            for row in cursor:
                (group_id, group_name) = row
                list.append(Group(id=group_id, name=group_name))
        finally:
            cursor.close()
        return list

    def show_all_contacts_in_group(self, group):
        l = list(db.get_contacts_in_group(group))
        return l

    def show_random_contact_from_group(self, group):
        l = db.get_contacts_in_group(group)
        random_contact = random.choice(l)
        return random_contact

    def find_group_with_contact(self):
        group_list = list(db.get_group_list())
        for el in group_list:
            if db.get_contacts_in_group(el):
                return el
        print(el)

    def destroy(self):
        self.connection.close()
