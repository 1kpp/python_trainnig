

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def login(self, username, password):
        self.app.open_home_page()
        wd = self.app.wd
        # enter login, password and submit
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()