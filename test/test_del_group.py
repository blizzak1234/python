from model.group import Group
import random

def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="77", header="77", footer="77"))
    old_groups = db.get_group_list()
    #index = randrange(len(old_groups))
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    #if check_ui:
    #    assert new_groups == app.group.get_group_list()