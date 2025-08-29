from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.patch import PatchCreate, PatchOut
from ..services.patch_service import create_patch, list_patches, mark_deployed

router = APIRouter()

@router.post("/", response_model=PatchOut)
def create(patch: PatchCreate, db: Session = Depends(get_db)):
    return create_patch(db, patch)

@router.get("/", response_model=list[PatchOut])
def all(db: Session = Depends(get_db)):
    return list_patches(db)

@router.post("/{patch_id}/deployed", response_model=PatchOut)
def deployed(patch_id: int, db: Session = Depends(get_db)):
    return mark_deployed(db, patch_id)
