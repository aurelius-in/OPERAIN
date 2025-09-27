from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.orm import Session
import json

from api.core.db import get_db_session
from api.models.webhook_event import WebhookEvent
from api.models.bom_item import BomItem
from api.models.incident import Incident
from api.models.eval_report import EvalReport
from api.models.release import Release


router = APIRouter(prefix="/webhooks", tags=["webhooks"]) 


@router.post("/{source}")
async def receive_webhook(source: str, request: Request, db: Session = next(get_db_session())):
	try:
		payload = await request.json()
	except Exception as e:
		raise HTTPException(status_code=400, detail="Invalid JSON") from e

	# store raw event
	event = WebhookEvent(source=source, event_type=str(payload.get("event")), payload_json=json.dumps(payload))
	db.add(event)

	# naive handlers per minimal contracts
	if source == "baywalk" and payload.get("event") == "bom.ready":
		project_id = int(payload.get("project_id", 0))
		for item in payload.get("items", []):
			bi = BomItem(
				project_id=project_id,
				sku=item.get("sku", ""),
				description=item.get("description", ""),
				qty=item.get("qty", 1),
				alt_sku=item.get("alt_sku", ""),
			)
			db.add(bi)

	if source == "edgesight" and payload.get("event") == "fail.detected":
		inc = Incident(
			project_id=int(payload.get("project_id", 0)),
			source="edgesight",
			sku=payload.get("sku", ""),
			image_url=payload.get("image_url", ""),
			log_url=payload.get("log_url", ""),
		)
		db.add(inc)

	if source == "rainlane" and payload.get("event") == "answer.yellow":
		inc = Incident(
			project_id=int(payload.get("project_id", 0)),
			source="rainlane",
			sku=payload.get("sku", ""),
		)
		db.add(inc)

	if source == "perceptionlab" and payload.get("event") == "eval.completed":
		rep = EvalReport(
			model_version_id=payload.get("model_version_id"),
			url=payload.get("report_url", ""),
			map=payload.get("map"),
			iou=payload.get("iou"),
			idf1=payload.get("idf1"),
			latency_ms=payload.get("latency_ms"),
		)
		db.add(rep)

	if source == "drifthawk" and payload.get("event") == "release.signed":
		release_id = payload.get("release_id")
		if release_id:
			rel = db.get(Release, release_id)
			if rel:
				rel.signed_receipt_url = payload.get("signed_receipt_url", "")

	db.commit()
	return {"status": "ok"}

