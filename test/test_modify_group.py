from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="77", header="77", footer="77"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_info = Group(name="New group")
    group_info.id = group.id
    #group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group_info)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_groups = map(clean, new_groups)
        assert sorted(db_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
