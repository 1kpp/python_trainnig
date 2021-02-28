from model.group import Group


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
        self.fill_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups()
        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_section()
        # select first group
        self.select_first_group()
        # Submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups()
        self.group_cache = None

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_section()
        self.select_first_group()
        # click edit button
        wd.find_element_by_name("edit").click()
        # edit all the fields
        self.fill_form(group)
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_groups()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_group_section(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_section()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        # open modification form
        # fill group form
        self.fill_form(new_group_data)
        # submit modifications
        wd.find_element_by_name("update").click()
        self.return_to_groups()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_section()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_section()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

