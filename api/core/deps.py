from fastapi import Depends, HTTPException, status
from api.core.auth import get_current_user
from api.models.user import User


def require_roles(*allowed: str):
	def _checker(user: User = Depends(get_current_user)) -> User:
		if user.role not in allowed:
			raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
		return user
	return _checker

