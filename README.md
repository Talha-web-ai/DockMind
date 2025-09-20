# DockMind

This project contains two FastAPI services for an enterprise AI pipeline:

1. **Main API**: Serves health checks and orchestrates API calls.
2. **Model API**: Serves predictions from a pre-trained XGBoost model (`xgb_model.joblib`).

## Folder Structure

enterprise-ai-pipeline/
│
├─ Dockerfile.main # Dockerfile for main API
├─ Dockerfile.model # Dockerfile for model API
├─ docker-compose.yml # Compose file for both APIs
├─ models/
│ └─ xgb_model.joblib # Trained XGBoost model
├─ main.py # Main API
├─ model_api.py # Model API
├─ requirements.txt
└─ README.md


## Requirements

- Python 3.11+
- Docker & Docker Compose



## Quick Start

### 1. Build and run APIs
```bash
# In the project root
docker compose up -d --build
2. Stop APIs

docker compose down
3. Access APIs
Main API: http://localhost:8000/health

Model API: http://localhost:8001/predict

Notes
.dockerignore ensures venv/, __pycache__/, and logs are excluded from Docker images.

docker-compose.yml maps ports 8000 and 8001 to host for easy testing.

