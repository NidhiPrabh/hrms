from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str
    full_name: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
