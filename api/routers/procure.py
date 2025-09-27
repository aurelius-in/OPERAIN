from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import csv
import io
import json as jsonlib

from api.core.db import get_db_session
from api.models.bom_item import BomItem
from api.core.deps import require_roles
from api.models.asset import Asset
from api.models.po import PO


router = APIRouter(prefix="/procure", tags=["procure"]) 


@router.post("/import-bom")
async def import_bom(file: UploadFile = File(...), db: Session = Depends(get_db_session), _=Depends(require_roles("Engineer","Admin"))):
	content = await file.read()
	items = []
	if file.filename.endswith(".csv"):
		reader = csv.DictReader(io.StringIO(content.decode("utf-8")))
		for row in reader:
			items.append(row)
	else:
		items = jsonlib.loads(content)
	created = []
	for it in items:
		bi = BomItem(
			project_id=int(it.get("project_id", 0)),
			sku=it.get("sku", ""),
			description=it.get("description", ""),
			qty=int(it.get("qty", 1)),
			alt_sku=it.get("alt_sku", ""),
		)
		db.add(bi)
		created.append(bi)
	db.commit()
	return {"created": len(created)}


@router.get("/export-bom.csv")
def export_bom_csv(db: Session = Depends(get_db_session)):
	rows = db.query(BomItem).all()
	csv_lines = ["sku,description,qty,alt_sku"]
	for r in rows:
		csv_lines.append(f"{r.sku},{r.description},{r.qty},{r.alt_sku}")
	return "\n".join(csv_lines)


@router.get("/bom")
def list_bom(db: Session = Depends(get_db_session), _=Depends(require_roles("Operator","Engineer","Quality","Auditor","Admin"))):
	rows = db.query(BomItem).all()
	return rows


@router.get("/assets")
def list_assets(db: Session = Depends(get_db_session), _=Depends(require_roles("Operator","Engineer","Quality","Auditor","Admin"))):
	return db.query(Asset).all()


@router.post("/assets")
def create_asset(asset: dict, db: Session = Depends(get_db_session), _=Depends(require_roles("Engineer","Admin"))):
	a = Asset(**asset)
	db.add(a)
	db.commit()
	db.refresh(a)
	return a


@router.post("/provision/{asset_id}")
def provision_asset(asset_id: int, db: Session = Depends(get_db_session), _=Depends(require_roles("Engineer","Admin"))):
	a = db.get(Asset, asset_id)
	if not a:
		return {"status": "not_found"}
	a.status = "provisioned"
	db.commit()
	return {"status": "ok"}


@router.post("/discover-cameras")
def discover_cameras(endpoints: list[dict], _=Depends(require_roles("Engineer","Admin"))):
	# stub: accept and return
	return {"saved": len(endpoints)}


@router.post("/po")
def create_po(po: dict, db: Session = Depends(get_db_session), _=Depends(require_roles("Engineer","Admin"))):
	p = PO(project_id=int(po.get("project_id", 0)), body_json=jsonlib.dumps(po))
	db.add(p)
	db.commit()
	db.refresh(p)
	return p

