from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    critical = "critical"
    high = "high"
    medium = "medium"
    low = "low"

class AlertCreate(BaseModel):
    source: str
    message: str

class AlertOut(BaseModel):
    id: int
    source: str
    message: str
    priority: Priority
    status: str
    created_at: datetime
    class Config:
        from_attributes = True

class AlertUpdate(BaseModel):
    status: Optional[Literal["open", "in_progress", "closed"]] = None
