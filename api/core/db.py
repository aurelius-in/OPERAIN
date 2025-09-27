from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.core.config import settings


engine = create_engine(settings.database_url, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)


def get_db_session():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
