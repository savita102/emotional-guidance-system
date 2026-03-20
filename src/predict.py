import joblib
import numpy as np
from src.decision_engine import decide_action, decide_timing
from src.uncertainty import compute_uncertainty




def run_predictions(df, X):

    model_state = joblib.load("models/state_model.pkl")
    model_intensity = joblib.load("models/intensity_model.pkl")

    le = joblib.load("models/label_encoder.pkl")
    
    probs = model_state.predict_proba(X)
    state_nums = model_state.predict(X)
    states = le.inverse_transform(state_nums)
    confidence = np.max(probs, axis=1)
    
    intensities = model_intensity.predict(X)
    intensities = np.clip(np.round(intensities), 1, 5)
    
    results = []
    
    for i, row in df.iterrows():
        
        action = decide_action(states[i], intensities[i], row['stress_level'], row['energy_level'])
        timing = decide_timing(states[i], intensities[i], row['stress_level'], row['energy_level'], row['time_of_day'])
        
        uncertain = compute_uncertainty(confidence[i], row['stress_level'], row['energy_level'])
        
        results.append({
            "id": row['id'],
            "predicted_state": states[i],
            "predicted_intensity": int(intensities[i]),
            "confidence": float(confidence[i]),
            "uncertain_flag": uncertain,
            "what_to_do": action,
            "when_to_do": timing
        })
    
    return results