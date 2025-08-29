from sqlalchemy.orm import Session
from ..models.db_models import Alert, Priority
from ..schemas.alert import AlertCreate, AlertUpdate
from ..utils.ml import predict_priority

def to_out(alert: Alert) -> Alert:
    return alert

def create_alert(db: Session, payload: AlertCreate):
    pr = predict_priority(payload.message)
    alert = Alert(source=payload.source, message=payload.message, priority=Priority(pr))
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert

def list_alerts(db: Session):
    return db.query(Alert).order_by(Alert.created_at.desc()).all()

def get_alert(db: Session, alert_id: int):
    return db.query(Alert).filter(Alert.id == alert_id).first()

def update_alert_status(db: Session, alert_id: int, payload: AlertUpdate):
    alert = get_alert(db, alert_id)
    if payload.status:
        alert.status = payload.status
    db.commit()
    db.refresh(alert)
    return alert
