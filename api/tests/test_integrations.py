from fastapi.testclient import TestClient
from api.app import app


client = TestClient(app)


def test_integrations_health_ok():
	r = client.get('/integrations/health')
	assert r.status_code == 200
	assert isinstance(r.json(), dict)

