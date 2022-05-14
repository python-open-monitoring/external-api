import pytest

import settings
from apps.api.handlers import ping
from settings import POSTGRES_DB
from settings import POSTGRES_PASSWORD
from settings import POSTGRES_USER


class EmulateRequest:
    is_test = True
    headers = {"Authorization": "Bearer MonitoringTestJwtToken__4rCTMAsKrKTB8rYz"}
    method = "GET"


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
    }


@pytest.fixture
def db_access_without_rollback_and_truncate(request, django_db_setup, django_db_blocker):
    django_db_blocker.unblock()
    request.addfinalizer(django_db_blocker.restore)


@pytest.mark.django_db
def test_ping():

    request = EmulateRequest()
    request.body = r'{"ping":"hello"}'
    json_rs = ping(request)
    if "pong" in json_rs:
        assert True
    else:
        assert False
