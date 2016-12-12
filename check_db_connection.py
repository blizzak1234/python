import mysql.connector
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    # cursor = connection.cursor()
    # cursor.execute("select * from group_list") # курсор стартует на таблице груплист
    # бежит по строкам и извлекает всю информацию в список
    # for row in cursor.fetchall():
    #     print(row)
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
