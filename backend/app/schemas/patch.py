from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PatchCreate(BaseModel):
    product: str
    version: str
    cve: Optional[str] = None
    scheduled_at: Optional[datetime] = None

class PatchOut(BaseModel):
    id: int
    product: str
    version: str
    cve: Optional[str]
    scheduled_at: Optional[datetime]
    deployed: bool
    created_at: datetime
    class Config:
        from_attributes = True
