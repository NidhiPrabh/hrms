from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.crud.crud_user import user
from app.api.deps import get_db
from app.schemas.token import Token

router = APIRouter()

@router.post("/login/access-token", response_model=Token)
def login_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = user.authenticate(db, username=form_data.username, password=form_data.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return Token(access_token=create_access_token(db_user.username))
