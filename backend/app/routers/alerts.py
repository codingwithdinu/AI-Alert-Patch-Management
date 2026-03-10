from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.patch import Patch
from app.models.alert_rule import AlertRule
from app.models.alert_log import AlertLog
from app.schemas.alert_log import AlertLogOut
from app.services.alert_service import send_alerts_for_patch

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/logs", response_model=List[AlertLogOut])
def list_alert_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(AlertLog).order_by(AlertLog.created_at.desc()).offset(skip).limit(limit).all()

@router.post("/trigger/{patch_id}", status_code=200)
def trigger_alert(patch_id: int, db: Session = Depends(get_db)):
    patch = db.query(Patch).filter(Patch.id == patch_id).first()
    if not patch:
        raise HTTPException(status_code=404, detail="Patch not found")
    rules = db.query(AlertRule).filter(AlertRule.is_active == True).all()
    results = send_alerts_for_patch(patch, rules, db)
    return {"detail": "Alerts processed", "results": results}

@router.post("/trigger-all", status_code=200)
def trigger_all_alerts(db: Session = Depends(get_db)):
    patches = db.query(Patch).filter(Patch.is_alert_sent == False).all()
    rules = db.query(AlertRule).filter(AlertRule.is_active == True).all()
    total = 0
    for patch in patches:
        send_alerts_for_patch(patch, rules, db)
        total += 1
    return {"detail": f"Processed {total} patches"}
