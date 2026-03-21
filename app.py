import streamlit as st
import pandas as pd
import joblib
import numpy as np

from src.feature_engineering import transform_features
from src.decision_engine import decide_action, decide_timing
from src.uncertainty import compute_uncertainty

st.set_page_config(page_title="ArvyaX AI", layout="centered")

st.title("🧠 Emotional Guidance System")
st.markdown("Understand → Decide → Guide")

# -------------------------
# INPUTS
# -------------------------
text = st.text_area("📝 Journal Entry")

sleep = st.slider("😴 Sleep Hours", 0.0, 12.0, 6.0)
stress = st.slider("😣 Stress Level", 1, 10, 5)
energy = st.slider("⚡ Energy Level", 1, 10, 5)

time_of_day = st.selectbox(
    "⏰ Time of Day",
    ["morning", "afternoon", "evening", "night"]
)

# -------------------------
# LOAD MODELS
# -------------------------
@st.cache_resource
def load_models():
    model_state = joblib.load("models/model_state.pkl")
    model_intensity = joblib.load("models/model_intensity.pkl")
    tfidf = joblib.load("models/tfidf.pkl")
    scaler = joblib.load("models/scaler.pkl")
    le = joblib.load("models/label_encoder.pkl")
    return model_state, model_intensity, tfidf, scaler, le

# -------------------------
# PREDICTION
# -------------------------
if st.button("🔍 Analyze"):

    model_state, model_intensity, tfidf, scaler, le = load_models()

    data = pd.DataFrame([{
        "id": 1,
        "journal_text": text,
        "sleep_hours": sleep,
        "stress_level": stress,
        "energy_level": energy,
        "time_of_day": time_of_day
    }])

    X = transform_features(data, tfidf, scaler)

    probs = model_state.predict_proba(X)
    state_num = model_state.predict(X)
    classes = ['calm', 'focused', 'mixed', 'neutral', 'overwhelmed', 'restless']

    try:
        state = le.inverse_transform([state_num])[0]
    except:
        state = classes[int(state_num[0])]

    raw_conf = np.max(probs)
    confidence = float(np.round(raw_conf * 0.85 + 0.05, 2))

    intensity = model_intensity.predict(X)[0]
    intensity = int(np.clip(round(intensity), 1, 5))

    if confidence < 0.50:
        action = "pause_and_breathe"
    else:
        action = decide_action(state, intensity, stress, energy)
    timing = decide_timing(state, intensity, stress, energy, time_of_day)

    uncertain = compute_uncertainty(confidence, stress, energy)

    # -------------------------
    # OUTPUT
    # -------------------------
    st.subheader("🧾 Results")

    st.write(f"**Emotional State:** {state}")
    st.write(f"**Intensity:** {intensity}")
    st.write(f"**Confidence:** {confidence:.2f}")

    st.write(f"**Recommended Action:** {action}")
    st.write(f"**When:** {timing}")

    if uncertain == 1:
        st.warning("⚠️ Model is uncertain. Try adding more detail.")

    # Optional supportive message
    st.subheader("💬 Guidance")

    if confidence < 0.50:
        st.write(
            f"I'm not completely sure how you're feeling, "
            f"but it might help to try {action.replace('_',' ')} {timing.replace('_',' ')}."
    )
    else:
        st.write(
            f"You seem {state} right now. "
            f"It might help to try {action.replace('_',' ')} {timing.replace('_',' ')}."
    )