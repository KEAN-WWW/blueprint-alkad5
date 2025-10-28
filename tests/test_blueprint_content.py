"""Tests for homepage and about content using Flask Blueprint."""

# Disable specific Pylint warnings used in pytest fixtures and tests
# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest
from application.app import init_app


@pytest.fixture(name="client")
def client():
    """Provide a Flask test client from the app factory."""
    app = init_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_main_page_content(client):
    """Test homepage returns 200 and contains 'Blueprint' keyword."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Blueprint" in resp.data


def test_about_page_content(client):
    """Test about page returns 200 and contains 'Blueprint' keyword."""
    resp = client.get("/about")
    assert resp.status_code == 200
    assert b"Blueprint" in resp.data
