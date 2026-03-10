from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from sqlalchemy.sql import func
from app.database import Base

class Patch(Base):
    __tablename__ = "patches"

    id = Column(Integer, primary_key=True, index=True)
    patch_id = Column(String(64), unique=True, index=True, nullable=False)
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)
    severity = Column(String(32), nullable=False)
    cve_id = Column(String(64), nullable=True)
    vendor = Column(String(128), nullable=True)
    product = Column(String(128), nullable=True)
    version = Column(String(64), nullable=True)
    status = Column(String(32), default="pending")
    risk_score = Column(Float, default=0.0)
    is_alert_sent = Column(Boolean, default=False)
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())