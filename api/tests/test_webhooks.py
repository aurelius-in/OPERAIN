import json
import hmac
import hashlib

from fastapi.testclient import TestClient
from api.app import app
from api.core.config import settings


client = TestClient(app)


def test_webhook_signature_optional():
	payload = {"event": "bom.ready", "project_id": 1, "items": []}
	headers = {}
	r = client.post('/webhooks/baywalk', json=payload, headers=headers)
	assert r.status_code in (200, 401)


def test_webhook_signature_valid():
	body = json.dumps({"event": "bom.ready", "project_id": 1, "items": []}).encode('utf-8')
	sig = hmac.new(settings.webhook_secret.encode('utf-8'), body, hashlib.sha256).hexdigest()
	r = client.post('/webhooks/baywalk', data=body, headers={'Content-Type': 'application/json', 'X-Signature': sig})
	assert r.status_code == 200

