from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AlertLogOut(BaseModel):
    id: int
    patch_id: int
    rule_id: Optional[int] = None
    channel: str
    status: str
    message: Optional[str] = None
    error: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
