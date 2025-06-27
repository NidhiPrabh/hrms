from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.department import Department, DepartmentCreate
from app.crud.crud_department import department
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=Department)
def create_department(*, db: Session = Depends(get_db), dep_in: DepartmentCreate, current_user=Depends(get_current_user)):
    return department.create(db, dep_in)

@router.get("/", response_model=list[Department])
def list_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return department.get_multi(db, skip, limit)
