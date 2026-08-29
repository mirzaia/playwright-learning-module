"""Illustrative fixture data flow; run with pytest from this module."""
import pytest


@pytest.fixture
def order_id():
    # Setup is named and reusable; pytest calls this before a test needs it.
    return "ORD-1001"


def test_fixture_is_injected(order_id):
    # The parameter name is the connection between fixture and test.
    assert order_id.startswith("ORD-")
