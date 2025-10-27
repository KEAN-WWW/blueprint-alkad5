import pytest
from application.app import init_app

@pytest.fixture(name="client")
def client():
    app = init_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_main_page_content(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Blueprint" in resp.data

def test_about_page_content(client):
    resp = client.get("/about")
    assert resp.status_code == 200
    assert b"Blueprint" in resp.data
