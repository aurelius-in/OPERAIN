from typing import Any, Dict

import httpx

from api.core.config import settings


async def health_check() -> bool:
	url = settings.drifthawk_base_url.rstrip("/") + "/health"
	async with httpx.AsyncClient(timeout=5) as client:
		resp = await client.get(url)
		return resp.status_code == 200


def build_deeplink(path: str = "/") -> str:
	return settings.drifthawk_base_url.rstrip("/") + path


async def promote_release(project_id: int, model_version_id: int) -> Dict[str, Any]:
	url = settings.drifthawk_base_url.rstrip("/") + "/api/releases"
	payload = {"project_id": project_id, "model_version_id": model_version_id, "plan": "canary"}
	async with httpx.AsyncClient(timeout=10) as client:
		resp = await client.post(url, json=payload)
		resp.raise_for_status()
		return resp.json()

