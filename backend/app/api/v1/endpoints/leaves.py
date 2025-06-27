from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.leave import Leave, LeaveCreate
from app.crud.crud_leave import leave
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=Leave)
def create_leave(*, db: Session = Depends(get_db), leave_in: LeaveCreate, current_user=Depends(get_current_user)):
    if leave_in.end_date < leave_in.start_date:
        raise HTTPException(status_code=400, detail="end_date must be after start_date")
    return leave.create(db, leave_in)

@router.get("/", response_model=list[Leave])
def list_leaves(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return leave.get_multi(db, skip, limit)
