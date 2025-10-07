# Finalidade : Monitoramento + Recalibração automática
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# monitor.py
from train_model import train_model
from pre_process import preprocess
import pandas as pd
import joblib

def detect_anomalies(model, new_data):
    preds = model.predict(new_data)
    return preds

def retrain_if_needed(new_data, anomaly_rate=0.1):
    model = joblib.load("model.pkl")
    preds = detect_anomalies(model, new_data)
    if (preds == -1).mean() > anomaly_rate:
        print("Anomaly rate too high. Retraining model...")
        train_model(new_data)
