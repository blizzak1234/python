# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


# функция инициализирующая фикстуру
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group_name", header="group_logo", footer="group_comment"))
    app.session.logout()


def test_test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()