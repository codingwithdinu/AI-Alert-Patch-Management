from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ Add this
from .database import init_db
from .routes.alerts import router as alerts_router
from .routes.patches import router as patches_router
from .routes.health import router as health_router
from .utils.scheduler import start_scheduler

app = FastAPI(title="AI-powered Alert & Patch Management")

# ✅ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 👈 React frontend ka URL (without / at end)
    allow_credentials=True,
    allow_methods=["*"],   # 👈 All methods (GET, POST, PATCH, DELETE...)
    allow_headers=["*"],   # 👈 All headers allowed (Content-Type, Authorization etc.)
)

# Routers include
app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(alerts_router, prefix="/alerts", tags=["alerts"])
app.include_router(patches_router, prefix="/patches", tags=["patches"])

@app.on_event("startup")
def on_startup():
    init_db()
    start_scheduler()
