from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_client_page():
    client = app.test_client()
    response = client.get("/client")
    assert response.status_code == 200