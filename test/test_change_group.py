from model.group import Group

def test_test_change_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change(Group(name="group_name_ch", header="group_logo_ch", footer="group_comment_ch"))
    app.session.logout()