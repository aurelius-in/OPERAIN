from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.core.config import settings
from api.core.db import get_db_session
from api.core.auth import create_access_token, get_current_user
from api.models.user import User


router = APIRouter(prefix="/auth", tags=["auth"]) 


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
	if not settings.allow_local_login:
		raise HTTPException(status_code=403, detail="Local login disabled")
	# Dev-only: if user doesn't exist, create on first login
	user = db.query(User).filter(User.email == form_data.username).first()
	if not user:
		user = User(email=form_data.username, role="Operator", name=form_data.username)
		db.add(user)
		db.commit()
		db.refresh(user)
	# No password check in dev mode
	token = create_access_token(subject=user.email, role=user.role)
	return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
def me(user: User = Depends(get_current_user)):
	return {"email": user.email, "role": user.role, "name": user.name}

