from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="77", header="77", footer="77"))
    app.group.delete_first_group()
