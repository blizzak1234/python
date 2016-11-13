# данный фаил позволяет использовать фикстуру во всех вспомогательных методах
import pytest
from fixture.application import Application


# функция инициализирующая фикстуру
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture