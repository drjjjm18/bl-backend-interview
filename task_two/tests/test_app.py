import json


def test_response(client):
    r = client.post('/', json={'city': 'London'})
    assert 200 == r.status_code


def test_temp(client):
    r = client.post('/', json={'city': 'London'})
    assert isinstance(json.loads(r.data)['temp'], int)


def test_error_city(client):
    r = client.post('/', json={'city': 'a'})
    assert 'Error' in json.loads(r.data)['temp']


def test_bad_http_method(client):
    r = client.get('/')
    assert r.status_code == 405
