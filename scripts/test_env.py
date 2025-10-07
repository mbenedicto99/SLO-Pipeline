# test_env.py

import mlflow
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_blobs

print("✅ Bibliotecas importadas com sucesso!")

# Gerar dados de exemplo
X, _ = make_blobs(n_samples=100, centers=1, cluster_std=0.5, random_state=42)

# Treinar modelo de exemplo
model = IsolationForest(n_estimators=50)
model.fit(X)

print("✅ Modelo treinado com sucesso!")

# Log no MLflow local
mlflow.set_experiment("Teste_MLOps")
with mlflow.start_run():
    mlflow.log_param("n_estimators", 50)
    mlflow.sklearn.log_model(model, "model")
    print("✅ Modelo logado no MLflow!")
