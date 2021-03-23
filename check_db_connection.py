import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get(Group(id=858))
    for item in l:
        print(item)
finally:
    pass # db.destroy()