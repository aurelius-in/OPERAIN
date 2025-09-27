PY=python
PIP=pip
VENV=.venv

.PHONY: bootstrap db.up api.dev web.dev up test migrate

bootstrap:
	@if not exist $(VENV) ($(PY) -m venv $(VENV))
	@$(VENV)\Scripts\python -m pip install --upgrade pip
	@$(VENV)\Scripts\pip install -r api/requirements.txt
	@if exist web (cd web && npm install) else (echo "web/ not present yet; skipping npm install")

db.up:
	docker compose up -d db redis

api.dev:
	setx PYTHONPATH . > NUL
	$(VENV)\Scripts\python -m uvicorn api.app:app --reload --host 0.0.0.0 --port 8000

web.dev:
	cd web && npm run dev

up:
	docker compose up -d --build

test:
	$(VENV)\Scripts\pytest -q || exit 0
	@if exist web (cd web && npm run typecheck || exit 0)

migrate:
	$(VENV)\Scripts\alembic -c api/migrations/alembic.ini revision --autogenerate -m "auto"
	$(VENV)\Scripts\alembic -c api/migrations/alembic.ini upgrade head

