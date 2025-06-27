from sqlalchemy.orm import Session
from app.db.base import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password

class CRUDUser:
    def create(self, db: Session, obj_in: UserCreate):
        db_obj = User(
            username=obj_in.username,
            full_name=obj_in.full_name,
            hashed_password=hash_password(obj_in.password),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, username: str, password: str):
        user = db.query(User).filter(User.username == username).first()
        if user and verify_password(password, user.hashed_password):
            return user
        return None

user = CRUDUser()
