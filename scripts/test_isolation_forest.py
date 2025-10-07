# test_isolation_forest.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_blobs
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

print("✅ Bibliotecas importadas com sucesso!")

# Gerar dados com blobs
X, _ = make_blobs(n_samples=300, centers=[[0, 0], [5, 5]], cluster_std=0.8, random_state=42)

# Adicionar outliers
rng = np.random.RandomState(42)
n_outliers = 30
outliers = rng.uniform(low=-6, high=10, size=(n_outliers, 2))
X = np.concatenate([X, outliers], axis=0)

# Criar labels para visualização
labels = np.array([1]*300 + [-1]*n_outliers)

# Treinar modelo Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)
preds = model.predict(X)

# Visualizar
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=preds, cmap='coolwarm', edgecolors='k')
plt.title("Detecção de Anomalias com Isolation Forest")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("isolation_forest_plot.png")
plt.show()
print("📊 Gráfico salvo como 'isolation_forest_plot.png'")

# Log no MLflow
mlflow.set_experiment("IsolationForest_2D")
with mlflow.start_run():
    mlflow.log_param("contamination", 0.1)
    mlflow.log_param("n_outliers", n_outliers)
    mlflow.log_metric("num_detected_anomalies", int((preds == -1).sum()))

    # Log do modelo com assinatura
    signature = infer_signature(X, preds)
    mlflow.sklearn.log_model(model, "model", signature=signature, input_example=X[:2])

    # Logar artefato (gráfico)
    mlflow.log_artifact("isolation_forest_plot.png")

    print("✅ Modelo e gráfico logados no MLflow com sucesso!")