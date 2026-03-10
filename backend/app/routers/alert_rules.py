from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.alert_rule import AlertRule
from app.schemas.alert_rule import AlertRuleCreate, AlertRuleUpdate, AlertRuleOut

router = APIRouter(prefix="/alert-rules", tags=["Alert Rules"])

@router.get("/", response_model=List[AlertRuleOut])
def list_rules(db: Session = Depends(get_db)):
    return db.query(AlertRule).all()

@router.post("/", response_model=AlertRuleOut, status_code=201)
def create_rule(payload: AlertRuleCreate, db: Session = Depends(get_db)):
    rule = AlertRule(**payload.model_dump())
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule

@router.patch("/{rule_id}", response_model=AlertRuleOut)
def update_rule(rule_id: int, payload: AlertRuleUpdate, db: Session = Depends(get_db)):
    rule = db.query(AlertRule).filter(AlertRule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Alert rule not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(rule, field, value)
    db.commit()
    db.refresh(rule)
    return rule

@router.delete("/{rule_id}", status_code=204)
def delete_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.query(AlertRule).filter(AlertRule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Alert rule not found")
    db.delete(rule)
    db.commit()

