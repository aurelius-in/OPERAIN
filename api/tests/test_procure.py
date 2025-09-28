from fastapi.testclient import TestClient
from api.app import app
from api.core.db import SessionLocal
from api.models.project import Project
from api.models.site import Site
from api.models.user import User


client = TestClient(app)


def test_health():
	r = client.get('/health')
	assert r.status_code == 200
	assert r.json().get('status') == 'ok'


def auth_headers(email: str = 'engineer@example.com'):
	# login to get token
	r = client.post('/auth/login', data={'username': email, 'password': 'dev'}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
	assert r.status_code == 200
	# elevate role in DB for this test
	db = SessionLocal()
	try:
		user = db.query(User).filter(User.email == email).first()
		user.role = 'Engineer'
		db.commit()
	finally:
		db.close()
	return {'Authorization': f"Bearer {r.json()['access_token']}"}


def test_create_asset_and_list():
	h = auth_headers()
	r = client.post('/procure/assets', json={'project_id': 1, 'type': 'edge', 'serial': 'EDG-42', 'status': 'new'}, headers=h)
	assert r.status_code == 200
	asset = r.json()
	assert asset['id'] > 0
	res = client.get('/procure/assets', headers=h)
	assert res.status_code == 200
	assert any(a['serial'] == 'EDG-42' for a in res.json())


def test_import_bom_json():
	# ensure a project exists to satisfy FK
	db = SessionLocal()
	try:
		s = Site(name='Test Site', timezone='UTC')
		db.add(s)
		db.flush()
		p = Project(site_id=s.id, name='Test', status='active')
		db.add(p)
		db.commit()
		db.refresh(p)
		project_id = p.id
	finally:
		db.close()

	h = auth_headers()
	content = b'[ {"project_id": %d, "sku": "CAM-X", "description": "Camera", "qty": 1 } ]' % project_id
	files = { 'file': ('bom.json', content, 'application/json') }
	r = client.post('/procure/import-bom', files=files, headers=h)
	assert r.status_code == 200
	assert r.json().get('created', 0) >= 1

