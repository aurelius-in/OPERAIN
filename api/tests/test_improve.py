from fastapi.testclient import TestClient
from api.app import app


client = TestClient(app)


def test_incidents_list():
	r = client.get('/improve/incidents')
	assert r.status_code == 200

