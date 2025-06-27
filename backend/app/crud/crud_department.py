from sqlalchemy.orm import Session
from app.db.base import Department
from app.schemas.department import DepartmentCreate

class CRUDDepartment:
    def create(self, db: Session, obj_in: DepartmentCreate):
        db_obj = Department(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, skip=0, limit=100):
        return db.query(Department).offset(skip).limit(limit).all()

department = CRUDDepartment()
