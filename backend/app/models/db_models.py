from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, Boolean
from sqlalchemy.sql import func
from ..database import Base
import enum

class Priority(str, enum.Enum):
    critical = "critical"
    high = "high"
    medium = "medium"
    low = "low"

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    priority = Column(Enum(Priority), nullable=False, default=Priority.low)
    status = Column(String(20), default="open")   # open | in_progress | closed
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Patch(Base):
    __tablename__ = "patches"
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String(100), nullable=False)   # OS/App name
    version = Column(String(50), nullable=False)
    cve = Column(String(50), nullable=True)
    scheduled_at = Column(DateTime(timezone=True), nullable=True)
    deployed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())