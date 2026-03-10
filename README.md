# 🤖 AI Alert & Patch Management System

A full-stack, AI-powered platform for managing security alerts and software patches. Built with **FastAPI** (Python) on the backend, **React + Vite** on the frontend, and a lightweight **ML model** for risk scoring.

---

## ✨ Features

| Area | Capability |
|------|-----------|
| 🔐 **Patch Management** | Create, schedule, and mark patches as deployed |
| 🚨 **Alert System** | Rule-based alerting with email & Slack notifications |
| 🤖 **AI / ML** | Risk-score patches automatically using scikit-learn |
| 📊 **Dashboard** | React dashboard with live patch & alert lists |
| ⏰ **Scheduler** | Background job (APScheduler) scans unalerted patches every 10 min |
| 🐳 **Docker** | One-command local setup via Docker Compose |

---

## 🗂️ Project Structure

```
AI-Alert-Patch-Management/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app entry-point
│   │   ├── config.py        # Pydantic-Settings config (reads .env)
│   │   ├── database.py      # SQLAlchemy engine / session
│   │   ├── models/          # ORM models (Patch, AlertRule, AlertLog)
│   │   ├── schemas/         # Pydantic request/response schemas
│   │   ├── routes/          # FastAPI routers (alerts, patches, health)
│   │   ├── services/        # Business logic (alert_service, patch_service)
│   │   └── utils/           # scheduler, helpers
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # Root component
│   │   ├── components/      # PatchList, PatchForm, AlertForm …
│   │   └── services/api.js  # Axios / fetch wrapper
│   ├── package.json
│   └── vite.config.js
├── ml/                      # Model training & inference scripts
├── automation/              # Automation helpers / scripts
├── config/                  # Extra config files
├── scripts/                 # Utility scripts
├── tests/                   # pytest test suite
├── docs/                    # Architecture diagrams, API docs
├── docker-compose.yml
├── render.yaml              # Render.com one-click deploy
└── .env                     # Local secrets (never commit!)
```

---

## 🚀 Quick Start (Docker)

```bash
# 1. Clone
git clone https://github.com/codingwithdinu/AI-Alert-Patch-Management.git
cd AI-Alert-Patch-Management

# 2. Configure secrets
cp .env.example .env
# Edit .env with your SMTP / Slack credentials

# 3. Start everything
docker compose up --build
```

| Service | URL |
|---------|-----|
| Backend API | http://localhost:8000 |
| API Docs (Swagger) | http://localhost:8000/docs |
| React Frontend | http://localhost:3000 |

---

## 🛠️ Local Development (without Docker)

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev          # Vite dev server at http://localhost:3000
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root (or in `backend/`):

```dotenv
# Database
DATABASE_URL=sqlite:///./data/patches.db

# Email alerts (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@gmail.com
SMTP_PASSWORD=your_app_password
ALERT_FROM_EMAIL=your@gmail.com
ALERT_TO_EMAIL=receiver@example.com

# Slack alerts (optional)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...

# App
DEBUG=false
```

---

## 🌐 API Reference

Full interactive docs available at `/docs` (Swagger UI) or `/redoc` when the server is running.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/patches` | List all patches |
| `POST` | `/patches` | Create a new patch |
| `PATCH` | `/patches/{id}/deploy` | Mark a patch as deployed |
| `GET` | `/alerts/logs` | List alert logs |
| `POST` | `/alerts/trigger/{patch_id}` | Trigger alerts for a patch |
| `POST` | `/alerts/trigger-all` | Trigger alerts for all pending patches |

---

## 🧪 Running Tests

```bash
cd backend
pytest tests/ -v
```

---

## ☁️ Deploy to Render.com

A `render.yaml` is included for one-click deployment to [Render.com](https://render.com).

1. Push this repo to GitHub.
2. Go to [render.com](https://render.com) → **New** → **Blueprint**.
3. Connect your repository.
4. Set the secret env vars (`SMTP_PASSWORD`, `SLACK_WEBHOOK_URL`, etc.) in the Render dashboard.
5. Click **Deploy**.

---

## 🤝 Contributing

Pull requests are welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "feat: add my feature"`
4. Push and open a PR

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.