# test_env2.py

import mlflow
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_blobs
from mlflow.models.signature import infer_signature

print("✅ Bibliotecas importadas com sucesso!")

# Gerar dados de exemplo
X, _ = make_blobs(n_samples=100, centers=1, cluster_std=0.5, random_state=42)

# Treinar modelo
model = IsolationForest(n_estimators=50)
model.fit(X)
print("✅ Modelo treinado com sucesso!")

# Inferir assinatura e exemplo de entrada
signature = infer_signature(X, model.predict(X))
input_example = X[:2]

# Log no MLflow
mlflow.set_experiment("Teste_MLOps_Signature")
with mlflow.start_run():
    mlflow.log_param("n_estimators", 50)
    mlflow.sklearn.log_model(
        model,
        "model",
        signature=signature,
        input_example=input_example
    )
    print("✅ Modelo logado com assinatura no MLflow!")

