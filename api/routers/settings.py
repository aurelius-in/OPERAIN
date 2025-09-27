from fastapi import APIRouter

from api.core.config import settings


router = APIRouter(prefix="/settings", tags=["settings"]) 


@router.get("")
def get_settings():
	return {
		"baywalk_base_url": settings.baywalk_base_url,
		"perceptionlab_base_url": settings.perceptionlab_base_url,
		"edgesight_base_url": settings.edgesight_base_url,
		"rainlane_base_url": settings.rainlane_base_url,
		"drifthawk_base_url": settings.drifthawk_base_url,
		"use_redis": settings.use_redis,
		"allow_local_login": settings.allow_local_login,
	}

