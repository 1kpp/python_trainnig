import pymysql.cursors(host="127.0.0.1", database="addressbook", user="root", password="")


connection = pymysql.connect

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor:
        print(row)
finally:
    connection.close()