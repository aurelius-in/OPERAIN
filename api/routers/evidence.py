from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.core.db import get_db_session
from api.services.locker import search_evidence, fetch_by_ref


router = APIRouter(prefix="/evidence", tags=["evidence"]) 


@router.get("/search")
def search(project_id: Optional[int] = None, sku: Optional[str] = None, batch: Optional[str] = None, db: Session = Depends(get_db_session)):
	return search_evidence(db, project_id=project_id, sku=sku, batch=batch)


@router.get("/{ref}")
def get_ref(ref: str, db: Session = Depends(get_db_session)):
	return fetch_by_ref(db, ref) or {"status": "not_found"}

