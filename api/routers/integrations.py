from fastapi import APIRouter
import httpx

from api.core.config import settings


router = APIRouter(prefix="/integrations", tags=["integrations"])


@router.get("/health")
async def integrations_health():
	services = {
		"baywalk": settings.baywalk_base_url,
		"perceptionlab": settings.perceptionlab_base_url,
		"edgesight": settings.edgesight_base_url,
		"rainlane": settings.rainlane_base_url,
		"drifthawk": settings.drifthawk_base_url,
	}
	results = {}
	async with httpx.AsyncClient(timeout=5) as client:
		for name, base in services.items():
			url = base.rstrip("/") + "/health"
			status = "red"
			try:
				resp = await client.get(url)
				if resp.status_code == 200:
					body = resp.json() if resp.headers.get("content-type", "").startswith("application/json") else {}
					if body.get("status") in ("ok", "healthy", "green"):
						status = "green"
					else:
						status = "yellow"
			except Exception:
				status = "red"
			results[name] = {"status": status}
	return results

