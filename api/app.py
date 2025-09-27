from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.logging import configure_logging
from api.routers import health
from api.routers import procure, improve, integrations, webhooks, evidence


def create_app() -> FastAPI:
	configure_logging()
	app = FastAPI(title="OPERAIN API")
	app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)
	app.include_router(health.router)
	app.include_router(procure.router)
	app.include_router(improve.router)
	app.include_router(integrations.router)
	app.include_router(webhooks.router)
	app.include_router(evidence.router)
	return app


app = create_app()
