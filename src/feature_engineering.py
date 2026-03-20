from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack

# TRAINING
def fit_features(df):
    
    tfidf = TfidfVectorizer(max_features=5000)
    X_text = tfidf.fit_transform(df['journal_text'])
    
    meta_cols = ['sleep_hours', 'stress_level', 'energy_level']
    X_meta = df[meta_cols].values
    
    scaler = StandardScaler()
    X_meta = scaler.fit_transform(X_meta)
    
    X = hstack([X_text, X_meta])
    
    return X, tfidf, scaler


# TESTING / INFERENCE
def transform_features(df, tfidf, scaler):
    
    X_text = tfidf.transform(df['journal_text'])
    
    meta_cols = ['sleep_hours', 'stress_level', 'energy_level']
    X_meta = scaler.transform(df[meta_cols].values)
    
    X = hstack([X_text, X_meta])
    
    return X