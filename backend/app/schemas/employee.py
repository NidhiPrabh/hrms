from pydantic import BaseModel, ConfigDict
from datetime import date

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    join_date: date
    department_id: int | None = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
