import pymysql.connections
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id="21"))
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
