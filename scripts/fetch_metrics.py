# Finalidade : Captura de métricas do Prometheus
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# fetch_metrics.py
import requests
import pandas as pd

PROMETHEUS = "http://localhost:9090"

def query_prometheus(metric_name):
    response = requests.get(f"{PROMETHEUS}/api/v1/query", params={'query': metric_name})
    data = response.json()['data']['result']
    rows = []
    for item in data:
        rows.append({
            'metric': item['metric'],
            'value': float(item['value'][1])
        })
    return pd.DataFrame(rows)
