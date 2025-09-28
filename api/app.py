from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.logging import configure_logging
from api.core.config import settings
from api.models.base import Base
# import models so SQLAlchemy sees all tables
from api.models import site as _m_site, project as _m_project, bom_item as _m_bom_item, asset as _m_asset, model_version as _m_model_version, eval_report as _m_eval_report, incident as _m_incident, capa as _m_capa, release as _m_release, user as _m_user, webhook_event as _m_webhook_event, po as _m_po  # noqa: F401
from api.core.db import engine
from api.routers import health
from api.routers import procure, improve, integrations, webhooks, evidence, auth, settings as settings_router


def create_app() -> FastAPI:
	configure_logging()
	app = FastAPI(title="OPERAIN API")
	allowed = [o.strip() for o in settings.allowed_cors_origins.split(',') if o.strip()]
	app.add_middleware(
		CORSMiddleware,
		allow_origins=allowed or ["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)
	# In testing mode, auto-create tables for sqlite
	if settings.testing:
		Base.metadata.create_all(bind=engine)
	app.include_router(health.router)
	app.include_router(procure.router)
	app.include_router(improve.router)
	app.include_router(integrations.router)
	app.include_router(webhooks.router)
	app.include_router(evidence.router)
	app.include_router(auth.router)
	app.include_router(settings_router.router)
	return app


app = create_app()
