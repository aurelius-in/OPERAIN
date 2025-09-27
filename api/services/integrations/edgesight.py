import httpx
from api.core.config import settings


async def health_check() -> bool:
	url = settings.edgesight_base_url.rstrip("/") + "/health"
	async with httpx.AsyncClient(timeout=5) as client:
		resp = await client.get(url)
		return resp.status_code == 200


def build_deeplink(path: str = "/") -> str:
	return settings.edgesight_base_url.rstrip("/") + path

