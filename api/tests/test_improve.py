from fastapi.testclient import TestClient
from api.app import app


client = TestClient(app)


def test_incidents_list():
	# authenticate as Operator to read incidents
	login = client.post('/auth/login', data={'username': 'operator@example.com', 'password': 'dev'}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
	assert login.status_code == 200
	headers = {'Authorization': f"Bearer {login.json()['access_token']}"}
	r = client.get('/improve/incidents', headers=headers)
	assert r.status_code == 200

