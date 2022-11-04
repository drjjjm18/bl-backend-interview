

def test_post(client):
    r = client.post('/', json={'city': 'London'})
    assert r.status_code == 200
