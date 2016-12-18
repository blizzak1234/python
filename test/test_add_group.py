# -*- coding: utf-8 -*-
from model.group import Group
from data.groups import testdata
import pytest



@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, db, group, check_ui):
    old_groups = db.get_group_list()
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
        # def clean(group):
        #     return Group(id=group.id, name=group.name.strip())
        # cleared_db_groups = map(clean, new_groups)
        # assert sorted(cleared_db_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
