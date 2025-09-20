from fastapi import FastAPI
from pydantic import BaseModel
import logging

# ------------------------
# Logger setup
# ------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# ------------------------
# FastAPI App
# ------------------------
app = FastAPI(title="Enterprise AI Pipeline", version="1.0.0")

# ------------------------
# Pydantic Model
# ------------------------
class PredictionRequest(BaseModel):
    feature1: float
    feature2: float
    feature3: float

# ------------------------
# Routes
# ------------------------
@app.get("/health")
def health_check():
    logger.info("Health check requested.")
    return {"status": "ok", "message": "API is healthy"}

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        logger.info(f"Received request: {request.dict()}")
        # Dummy prediction (sum of features)
        result = request.feature1 + request.feature2 + request.feature3
        return {"prediction": result}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return {"error": str(e)}
