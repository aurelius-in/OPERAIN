from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.core.db import get_db_session
from api.models.incident import Incident
from api.models.capa import Capa
from api.models.eval_report import EvalReport
from api.models.release import Release


router = APIRouter(prefix="/improve", tags=["improve"]) 


@router.get("/incidents")
def list_incidents(db: Session = Depends(get_db_session)):
	return db.query(Incident).all()


@router.post("/incidents")
def create_incident(payload: dict, db: Session = Depends(get_db_session)):
	inc = Incident(**payload)
	db.add(inc)
	db.commit()
	db.refresh(inc)
	return inc


@router.patch("/incidents/{incident_id}")
def update_incident(incident_id: int, payload: dict, db: Session = Depends(get_db_session)):
	inc = db.get(Incident, incident_id)
	if not inc:
		return {"status": "not_found"}
	for k, v in payload.items():
		setattr(inc, k, v)
	db.commit()
	return {"status": "ok"}


@router.post("/capa")
def create_capa_from_incident(payload: dict, db: Session = Depends(get_db_session)):
	c = Capa(**payload)
	db.add(c)
	db.commit()
	db.refresh(c)
	return c


@router.patch("/capa/{capa_id}")
def update_capa(capa_id: int, payload: dict, db: Session = Depends(get_db_session)):
	c = db.get(Capa, capa_id)
	if not c:
		return {"status": "not_found"}
	for k, v in payload.items():
		setattr(c, k, v)
	db.commit()
	return {"status": "ok"}


@router.post("/retest/{incident_id}")
def retest_incident(incident_id: int, db: Session = Depends(get_db_session)):
	# stub: create an eval report
	rep = EvalReport(model_version_id=None, url="https://example.com/report.pdf", map=0.5, iou=0.6, idf1=0.7, latency_ms=30)
	db.add(rep)
	db.commit()
	db.refresh(rep)
	return rep


@router.post("/promote")
def promote_release(payload: dict, db: Session = Depends(get_db_session)):
	rel = Release(**payload)
	db.add(rel)
	db.commit()
	db.refresh(rel)
	return rel

