# Finalidade : Envio de alertas para Alertmanager
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# send_alert.py
import requests
import json

def send_alert(summary, description):
    alert = [{
        "labels": {
            "alertname": "SLOViolation",
            "severity": "critical"
        },
        "annotations": {
            "summary": summary,
            "description": description
        }
    }]
    response = requests.post("http://localhost:9093/api/v1/alerts", data=json.dumps(alert))
    print("Alert sent:", response.status_code)
