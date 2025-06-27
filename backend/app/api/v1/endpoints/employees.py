from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.employee import Employee, EmployeeCreate
from app.crud.crud_employee import employee
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=Employee)
def create_employee(*, db: Session = Depends(get_db), emp_in: EmployeeCreate, current_user=Depends(get_current_user)):
    return employee.create(db, emp_in)

@router.get("/", response_model=list[Employee])
def list_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return employee.get_multi(db, skip, limit)
