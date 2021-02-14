

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        # Create a new group
        wd = self.app.wd
        self.open_group_section()
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_section()
        #select first group
        wd.find_element_by_name("selected[]")
        #submit deletion
        wd.find_element_by_name("delete")
        self.return_to_groups()

    def open_group_section(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

