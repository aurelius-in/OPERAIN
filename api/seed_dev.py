from sqlalchemy.orm import Session
from api.core.db import SessionLocal
from api.models.site import Site
from api.models.project import Project
from api.models.bom_item import BomItem
from api.models.asset import Asset
from api.models.incident import Incident


def run():
	db: Session = SessionLocal()
	try:
		site = Site(name="Main Plant", timezone="UTC")
		db.add(site)
		db.flush()
		project = Project(site_id=site.id, name="Line A", status="active")
		db.add(project)
		db.flush()
		bom = [
			BomItem(project_id=project.id, sku="EDGE-BOX", description="Edge device", qty=2),
			BomItem(project_id=project.id, sku="CAM-123", description="Camera", qty=4),
		]
		for b in bom:
			db.add(b)
		assets = [
			Asset(project_id=project.id, type="edge", serial="EDG-0001", status="new"),
			Asset(project_id=project.id, type="camera", serial="CAM-0001", status="new"),
		]
		for a in assets:
			db.add(a)
		inc = Incident(project_id=project.id, source="manual", sku="CAM-123")
		db.add(inc)
		db.commit()
	finally:
		db.close()


if __name__ == "__main__":
	run()

