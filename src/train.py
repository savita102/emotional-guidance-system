from xgboost import XGBClassifier, XGBRegressor
import joblib
from sklearn.preprocessing import LabelEncoder
import os

def train_models(X, df, tfidf, scaler, le):

    os.makedirs("models", exist_ok=True)

    # -------------------------
    # ENCODE EMOTIONAL STATE
    # -------------------------
    le = LabelEncoder()
    y_state = df["emotional_state"]
    y_intensity = df["intensity"]

    model_state = XGBClassifier()
    model_intensity = XGBRegressor()

    model_state.fit(X, y_state)
    model_intensity.fit(X, y_intensity)

    # ✅ Save everything
    joblib.dump(model_state, "models/model_state.pkl")
    joblib.dump(model_intensity, "models/model_intensity.pkl")
    joblib.dump(tfidf, "models/tfidf.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(le, "models/label_encoder.pkl")