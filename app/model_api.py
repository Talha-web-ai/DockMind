from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path
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
# Globals
# ------------------------
MODEL = None
FEATURES: list[str] = []

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "xgb_model.pkl"

# ------------------------
# FastAPI app
# ------------------------
app = FastAPI(title="Enterprise AI Model API", version="1.0.0")

# ------------------------
# Pydantic Request Model
# ------------------------
class Payload(BaseModel):
    data: dict  # {"feature1": ..., "feature2": ..., ...}

# ------------------------
# Load model at startup
# ------------------------
@app.on_event("startup")
def load_model():
    global MODEL, FEATURES
    try:
        MODEL = joblib.load(MODEL_PATH)
        FEATURES = MODEL.feature_names_in_.tolist()
        logger.info(f"✅ Model loaded successfully with features: {FEATURES}")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")

# ------------------------
# Prediction endpoint
# ------------------------
@app.post("/predict")
def predict(payload: Payload):
    global MODEL, FEATURES
    try:
        logger.info(f"Received request: {payload.data}")
        input_df = pd.DataFrame([payload.data])
        input_df = input_df[FEATURES]  # Keep only features model expects
        prediction = MODEL.predict(input_df)
        logger.info(f"Prediction: {prediction.tolist()}")
        return {"prediction": prediction.tolist()}
    except KeyError as e:
        logger.error(f"Missing feature in request: {e}")
        return {"error": f"Missing feature: {e}"}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return {"error": str(e)}
