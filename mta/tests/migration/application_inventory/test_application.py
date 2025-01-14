import pytest

from mta.fixtures.application_inventory import json_application


@pytest.mark.parametrize("application", json_application(), indirect=True)
@pytest.mark.app
def test_create_app(application, get_api):
    app_from_db = get_api.applications_id_get(application.id)
    assert application.name == app_from_db.name
