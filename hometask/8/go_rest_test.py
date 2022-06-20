import pytest
from HttpClient import HttpClient
from Config import Config


@pytest.fixture
def client():
    config = Config('config.yaml')
    return HttpClient(config.get('base_url'), config.get('token'))


def test_get_users(client):
    response = client.get('/public-api/users')
    assert 200 == response.status_code
    assert len(response.json()['data']) > 0


def test_create_user(client):
    response = client.post('/public-api/users',
                           {'first_name': 'Basil', 'last_name': 'Pupkin', 'email': 'pupkin@sad.com'})
    assert 200 == response.status_code
