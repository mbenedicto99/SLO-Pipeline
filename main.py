# Finalidade : Modulo de Encadeamento
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# main.py
from fetch_metrics import query_prometheus
from pre_process import preprocess
from monitor import retrain_if_needed
import joblib

metric = "http_requests_total"
data = query_prometheus(metric)
processed = preprocess(data)
retrain_if_needed(processed)
