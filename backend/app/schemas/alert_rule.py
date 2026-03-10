from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AlertRuleBase(BaseModel):
    name: str
    severity_filter: Optional[str] = None
    min_risk_score: float = 0.0
    notify_email: bool = True
    notify_slack: bool = True
    is_active: bool = True

class AlertRuleCreate(AlertRuleBase):
    pass

class AlertRuleUpdate(BaseModel):
    name: Optional[str] = None
    severity_filter: Optional[str] = None
    min_risk_score: Optional[float] = None
    notify_email: Optional[bool] = None
    notify_slack: Optional[bool] = None
    is_active: Optional[bool] = None

class AlertRuleOut(AlertRuleBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
