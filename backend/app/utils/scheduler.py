from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from ..database import SessionLocal
from ..models.db_models import Patch

scheduler = BackgroundScheduler()

def _deploy_pending_patches():
    db = SessionLocal()
    try:
        now = datetime.utcnow()
        pending = db.query(Patch).filter(Patch.deployed == False).all()  # noqa: E712
        for p in pending:
            if p.scheduled_at and p.scheduled_at <= now:
                p.deployed = True  # simulate deployment
        db.commit()
    finally:
        db.close()

def start_scheduler():
    if not scheduler.running:
        scheduler.add_job(_deploy_pending_patches, "interval", seconds=15, id="patch_deployer", replace_existing=True)
        scheduler.start()
