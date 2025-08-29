from sqlalchemy.orm import Session
from ..models.db_models import Patch
from ..schemas.patch import PatchCreate

def create_patch(db: Session, payload: PatchCreate):
    patch = Patch(
        product=payload.product,
        version=payload.version,
        cve=payload.cve,
        scheduled_at=payload.scheduled_at
    )
    db.add(patch)
    db.commit()
    db.refresh(patch)
    return patch

def list_patches(db: Session):
    return db.query(Patch).order_by(Patch.created_at.desc()).all()

def mark_deployed(db: Session, patch_id: int):
    p = db.query(Patch).filter(Patch.id == patch_id).first()
    if not p:
        return None
    p.deployed = True
    db.commit()
    db.refresh(p)
    return p