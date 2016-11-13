from model.group import Group

def test_change_group(app):
    app.group.change(Group(name="group_name_ch", header="group_logo_ch", footer="group_comment_ch"))
