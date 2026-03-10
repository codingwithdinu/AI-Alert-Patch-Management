from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.patch import Patch
from app.schemas.patch import PatchCreate, PatchUpdate, PatchOut
from app.services.ml_service import score_patch

router = APIRouter(prefix="/patches", tags=["Patches"])

@router.get("/", response_model=List[PatchOut])
def list_patches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Patch).offset(skip).limit(limit).all()

@router.get("/{patch_id}", response_model=PatchOut)
def get_patch(patch_id: int, db: Session = Depends(get_db)):
    patch = db.query(Patch).filter(Patch.id == patch_id).first()
    if not patch:
        raise HTTPException(status_code=404, detail="Patch not found")
    return patch

@router.post("/", response_model=PatchOut, status_code=201)
def create_patch(payload: PatchCreate, db: Session = Depends(get_db)):
    existing = db.query(Patch).filter(Patch.patch_id == payload.patch_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Patch ID already exists")
    patch = Patch(**payload.model_dump())
    patch.risk_score = score_patch(patch)
    db.add(patch)
    db.commit()
    db.refresh(patch)
    return patch

@router.patch("/{patch_id}", response_model=PatchOut)
def update_patch(patch_id: int, payload: PatchUpdate, db: Session = Depends(get_db)):
    patch = db.query(Patch).filter(Patch.id == patch_id).first()
    if not patch:
        raise HTTPException(status_code=404, detail="Patch not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(patch, field, value)
    db.commit()
    db.refresh(patch)
    return patch

@router.delete("/{patch_id}", status_code=204)
def delete_patch(patch_id: int, db: Session = Depends(get_db)):
    patch = db.query(Patch).filter(Patch.id == patch_id).first()
    if not patch:
        raise HTTPException(status_code=404, detail="Patch not found")
    db.delete(patch)
    db.commit()

