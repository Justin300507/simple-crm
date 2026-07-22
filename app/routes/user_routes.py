from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.utils.auth import get_current_user

user_router = APIRouter()

@user_router.get("/users/me")
def get_current_user_details(current_user: Any = Depends(get_current_user), db: Session = Depends(get_db)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "display_name": getattr(current_user, "display_name", None)
    }