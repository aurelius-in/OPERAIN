from typing import Any, Dict, List, Optional

from sqlalchemy.orm import Session

from api.models.incident import Incident
from api.models.eval_report import EvalReport
from api.models.release import Release


def search_evidence(
	db: Session,
	project_id: Optional[int] = None,
	sku: Optional[str] = None,
	batch: Optional[str] = None,  # placeholder; not used in current schema
) -> List[Dict[str, Any]]:
	items: List[Dict[str, Any]] = []

	q_inc = db.query(Incident)
	if project_id is not None:
		q_inc = q_inc.filter(Incident.project_id == project_id)
	if sku:
		q_inc = q_inc.filter(Incident.sku == sku)
	for inc in q_inc.all():
		if inc.image_url:
			items.append({
				"ref": f"incident:{inc.id}",
				"type": "incident_snapshot",
				"url": inc.image_url,
				"project_id": inc.project_id,
				"sku": inc.sku,
				"created_at": inc.created_at.isoformat() if inc.created_at else None,
			})
		if inc.log_url:
			items.append({
				"ref": f"incident:{inc.id}",
				"type": "incident_log",
				"url": inc.log_url,
				"project_id": inc.project_id,
				"sku": inc.sku,
				"created_at": inc.created_at.isoformat() if inc.created_at else None,
			})

	# Eval reports (no project mapping in minimal schema)
	for rep in db.query(EvalReport).all():
		items.append({
			"ref": f"eval:{rep.id}",
			"type": "eval_report",
			"url": rep.url,
			"metrics": {"map": rep.map, "iou": rep.iou, "idf1": rep.idf1, "latency_ms": rep.latency_ms},
			"created_at": rep.created_at.isoformat() if rep.created_at else None,
		})

	# Releases (signed receipts)
	q_rel = db.query(Release)
	if project_id is not None:
		q_rel = q_rel.filter(Release.project_id == project_id)
	for rel in q_rel.all():
		if rel.signed_receipt_url:
			items.append({
				"ref": f"release:{rel.id}",
				"type": "signed_receipt",
				"url": rel.signed_receipt_url,
				"project_id": rel.project_id,
				"created_at": rel.created_at.isoformat() if rel.created_at else None,
			})

	# Sort newest first if timestamps exist
	items.sort(key=lambda x: x.get("created_at") or "", reverse=True)
	return items


def fetch_by_ref(db: Session, ref: str) -> Optional[Dict[str, Any]]:
	"""ref format: "incident:ID" | "eval:ID" | "release:ID""" 
	try:
		prefix, sid = ref.split(":", 1)
		id_val = int(sid)
	except Exception:
		return None

	if prefix == "incident":
		inc = db.get(Incident, id_val)
		if not inc:
			return None
		return {
			"ref": ref,
			"type": "incident",
			"image_url": inc.image_url,
			"log_url": inc.log_url,
			"project_id": inc.project_id,
			"sku": inc.sku,
			"created_at": inc.created_at.isoformat() if inc.created_at else None,
		}
	if prefix == "eval":
		rep = db.get(EvalReport, id_val)
		if not rep:
			return None
		return {
			"ref": ref,
			"type": "eval_report",
			"url": rep.url,
			"metrics": {"map": rep.map, "iou": rep.iou, "idf1": rep.idf1, "latency_ms": rep.latency_ms},
			"created_at": rep.created_at.isoformat() if rep.created_at else None,
		}
	if prefix == "release":
		rel = db.get(Release, id_val)
		if not rel:
			return None
		return {
			"ref": ref,
			"type": "signed_receipt",
			"url": rel.signed_receipt_url,
			"project_id": rel.project_id,
			"created_at": rel.created_at.isoformat() if rel.created_at else None,
		}
	return None

