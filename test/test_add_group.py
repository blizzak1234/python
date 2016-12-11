# -*- coding: utf-8 -*-
from model.group import Group
from data.groups import testdata
import pytest


<<<<<<< HEAD
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, db, group):
    old_groups = db.get_group_list()
=======

def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
>>>>>>> f39b12fad0daf873b4bf7dc31f76a6c59d3b9485
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
