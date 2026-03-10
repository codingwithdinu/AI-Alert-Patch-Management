from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PatchBase(BaseModel):
    patch_id: str
    title: str
    description: Optional[str] = None
    severity: str
    cve_id: Optional[str] = None
    vendor: Optional[str] = None
    product: Optional[str] = None
    version: Optional[str] = None
    published_at: Optional[datetime] = None

class PatchCreate(PatchBase):
    pass

class PatchUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    severity: Optional[str] = None
    status: Optional[str] = None
    risk_score: Optional[float] = None

class PatchOut(PatchBase):
    id: int
    status: str
    risk_score: float
    is_alert_sent: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
