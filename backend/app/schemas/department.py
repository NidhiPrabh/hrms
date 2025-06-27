from pydantic import BaseModel, ConfigDict

class DepartmentBase(BaseModel):
    name: str
    description: str | None = None

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
