import zad_1


def test_hello_world():
    client = zad_1.app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert response.get_json() == {"hello": "world"}
