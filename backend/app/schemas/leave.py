from pydantic import BaseModel, ConfigDict
from datetime import date

class LeaveBase(BaseModel):
    start_date: date
    end_date: date
    reason: str | None = None

class LeaveCreate(LeaveBase):
    employee_id: int

class Leave(LeaveBase):
    id: int
    status: str
    employee_id: int
    model_config = ConfigDict(from_attributes=True)
