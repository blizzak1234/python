# данный фаил позволяет использовать фикстуру во всех вспомогательных методах
import pytest
from fixture.application import Application


# функция инициализирующая фикстуру
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture