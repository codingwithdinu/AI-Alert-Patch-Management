from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.alert import AlertCreate, AlertOut, AlertUpdate
from ..services.alert_service import create_alert, list_alerts, update_alert_status, get_alert

router = APIRouter()

@router.post("/", response_model=AlertOut)
def create(alert: AlertCreate, db: Session = Depends(get_db)):
    return create_alert(db, alert)

@router.get("/", response_model=list[AlertOut])
def all(db: Session = Depends(get_db)):
    return list_alerts(db)

@router.patch("/{alert_id}", response_model=AlertOut)
def update(alert_id: int, payload: AlertUpdate, db: Session = Depends(get_db)):
    if get_alert(db, alert_id) is None:
        raise HTTPException(404, "Alert not found")
    return update_alert_status(db, alert_id, payload)
