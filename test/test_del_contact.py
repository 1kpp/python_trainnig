import time


def test_delete_contact(app):
    time.sleep(1)
    app.session.login(username="admin", password="secret")
    app.contact.delete()
    app.return_to_home_page()
    time.sleep(1)
    app.session.logout()