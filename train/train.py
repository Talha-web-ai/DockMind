# train/train.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb
import joblib
import os

# 1️⃣ Load dataset
dataset_path = "/home/luffy/enterprise-ai-pipeline/data/dataset.csv"

if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset not found at {dataset_path}")

df = pd.read_csv(dataset_path)

# Strip column names to avoid issues with spaces
df.columns = df.columns.str.strip()
print("Columns in dataset:", df.columns.tolist())

# 2️⃣ Set target column (replace with your actual target column name)
target_col = "y"  # <-- change this if your dataset uses a different name
if target_col not in df.columns:
    target_col = df.columns[-1]  # fallback: assume last column is the target
    print(f"Target column '{target_col}' inferred from last column.")

# 3️⃣ Split features and labels
X = df.drop(columns=[target_col])
y = df[target_col]

# 4️⃣ Encode labels if they are strings
if y.dtype == object:
    le = LabelEncoder()
    y = le.fit_transform(y)
    print(f"Classes after encoding: {le.classes_}")

# 5️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6️⃣ Train XGBoost classifier
model = xgb.XGBClassifier(
    objective="multi:softprob" if len(np.unique(y)) > 2 else "binary:logistic",
    eval_metric="mlogloss" if len(np.unique(y)) > 2 else "logloss",
    use_label_encoder=False
)
model.fit(X_train, y_train)

# 7️⃣ Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 8️⃣ Save model
model_path = "/home/luffy/enterprise-ai-pipeline/models/xgb_model.joblib"
os.makedirs(os.path.dirname(model_path), exist_ok=True)
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
