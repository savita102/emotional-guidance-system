from src.preprocess import load_and_clean
from src.feature_engineering import fit_features
from src.train import train_models
from sklearn.preprocessing import LabelEncoder

# Load data
train_df = load_and_clean("data/train.csv")

# ✅ Fit encoder BEFORE training
le = LabelEncoder()
train_df["emotional_state"] = le.fit_transform(train_df["emotional_state"])

# Debug (IMPORTANT)
print("Classes:", le.classes_)

# Features
X_train, tfidf, scaler = fit_features(train_df)

# Train + save
train_models(X_train, train_df, tfidf, scaler, le)

print("✅ Pipeline completed successfully!")