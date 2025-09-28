from fastapi.testclient import TestClient
from api.app import app


client = TestClient(app)


def test_settings_endpoint():
	r = client.get('/settings')
	assert r.status_code == 200
	data = r.json()
	assert 'baywalk_base_url' in data and 'allow_local_login' in data

