from sqlalchemy.orm import Session
from app.db.base import Employee
from app.schemas.employee import EmployeeCreate

class CRUDEmployee:
    def create(self, db: Session, obj_in: EmployeeCreate):
        db_obj = Employee(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, skip=0, limit=100):
        return db.query(Employee).offset(skip).limit(limit).all()

employee = CRUDEmployee()
