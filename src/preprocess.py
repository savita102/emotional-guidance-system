import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    
    df['journal_text'] = df['journal_text'].fillna("")
    df['sleep_hours'] = df['sleep_hours'].fillna(df['sleep_hours'].mean())
    df['stress_level'] = df['stress_level'].fillna(df['stress_level'].median())
    df['energy_level'] = df['energy_level'].fillna(df['energy_level'].median())
    
    return df