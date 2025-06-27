from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import User, UserCreate
from app.crud.crud_user import user
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=User)
def register_user(*, db: Session = Depends(get_db), user_in: UserCreate):
    return user.create(db, user_in)
