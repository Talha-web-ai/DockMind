import logging
from logging.handlers import RotatingFileHandler
import os

# ------------------------
# Create log directory if it doesn't exist
# ------------------------
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# ------------------------
# Configure logger
# ------------------------
logger = logging.getLogger("enterprise_ai_pipeline")
logger.setLevel(logging.INFO)

# Rotating file handler
file_handler = RotatingFileHandler(
    os.path.join(LOG_DIR, "app.log"),
    maxBytes=5*1024*1024,  # 5 MB
    backupCount=3
)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# ------------------------
# Example usage function
# ------------------------
def log_info(message: str):
    logger.info(message)
