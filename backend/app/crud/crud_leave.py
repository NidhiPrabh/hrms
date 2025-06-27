from sqlalchemy.orm import Session
from app.db.base import Leave
from app.schemas.leave import LeaveCreate

class CRUDLeave:
    def create(self, db: Session, obj_in: LeaveCreate):
        db_obj = Leave(status="Pending", **obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, skip=0, limit=100):
        return db.query(Leave).offset(skip).limit(limit).all()

leave = CRUDLeave()
