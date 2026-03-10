# AI Alert Patch Management

An AI-powered patch management system with automated alerting.

## Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React + Vite (JavaScript)
- **Database:** SQLite
- **Alerts:** Email (SMTP) + Slack Webhook
- **ML:** scikit-learn patch risk scoring

## Project Structure
```
.
├── backend/         # FastAPI backend
├── frontend/        # React + Vite frontend
├── ml/              # ML models for patch risk scoring
├── automation/      # Automation scripts
├── scripts/         # Utility scripts
├── config/          # Configuration files
├── tests/           # Tests
├── docs/            # Documentation
└── docker-compose.yml
```

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker (optional)

### Using Docker
```bash
docker-compose up --build
```

### Manual Setup

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables
Copy `.env.example` to `.env` and fill in the values.

## API Docs
Once backend is running, visit: http://localhost:8000/docs

## Features
- Patch inventory management
- AI-based patch risk scoring
- Real-time alerts via Email and Slack
- Dashboard with patch status overview
- Configurable alert rules
- Docker support