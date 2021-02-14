import time


def test_edit_first_group(app):
    time.sleep(1)
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group()
    time.sleep(1)
    app.session.logout()