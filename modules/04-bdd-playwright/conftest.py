pytest_plugins = ["commerce_portal.fixtures"]


import pytest


@pytest.fixture
def scenario_state():
    return {}
