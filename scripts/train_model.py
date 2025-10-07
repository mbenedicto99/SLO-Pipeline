# Finalidade : Treinamento com Isolation Forest
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# train_model.py
from sklearn.ensemble import IsolationForest
import joblib

def train_model(X, model_path="model.pkl"):
    model = IsolationForest(n_estimators=100, contamination=0.05)
    model.fit(X)
    joblib.dump(model, model_path)
    return model
