from typing import Any, Dict, Optional

import httpx

from api.core.config import settings


async def health_check() -> bool:
	url = settings.perceptionlab_base_url.rstrip("/") + "/health"
	async with httpx.AsyncClient(timeout=5) as client:
		resp = await client.get(url)
		return resp.status_code == 200 and resp.json().get("status") in ("ok", "healthy")


def build_deeplink(path: str = "/") -> str:
	return settings.perceptionlab_base_url.rstrip("/") + path


async def request_eval(incident_ref: Optional[str] = None, clip_url: Optional[str] = None) -> Dict[str, Any]:
	url = settings.perceptionlab_base_url.rstrip("/") + "/api/evals"
	payload: Dict[str, Any] = {}
	if incident_ref:
		payload["incident_ref"] = incident_ref
	if clip_url:
		payload["clip_url"] = clip_url
	async with httpx.AsyncClient(timeout=10) as client:
		resp = await client.post(url, json=payload)
		resp.raise_for_status()
		return resp.json()

