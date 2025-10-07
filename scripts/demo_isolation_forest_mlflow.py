# demo_isolation_forest_mlflow.py

"""
Demonstração completa de uso do Isolation Forest com MLflow.

✔ Gera dados com outliers
✔ Treina modelo de detecção de anomalias
✔ Visualiza resultado com gráfico
✔ Loga modelo, parâmetros, métricas e gráfico no MLflow
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_blobs
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

# 1. Gerar dados (2 clusters + outliers)
X, _ = make_blobs(n_samples=300, centers=[[0, 0], [5, 5]], cluster_std=0.8, random_state=42)
outliers = np.random.uniform(low=-6, high=10, size=(30, 2))
X_total = np.vstack([X, outliers])

# 2. Treinar modelo Isolation Forest
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X_total)
preds = model.predict(X_total)

# 3. Visualizar
plt.figure(figsize=(8, 6))
plt.scatter(X_total[:, 0], X_total[:, 1], c=preds, cmap="coolwarm", edgecolors="k")
plt.title("Detecção de Anomalias com Isolation Forest")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("if_demo_plot.png")
plt.show()

# 4. Logar no MLflow
mlflow.set_experiment("Demo_IsolationForest")
with mlflow.start_run():
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("contamination", 0.1)
    mlflow.log_metric("n_anomalies", int((preds == -1).sum()))

    signature = infer_signature(X_total, preds)
    mlflow.sklearn.log_model(model, "model", signature=signature, input_example=X_total[:2])
    mlflow.log_artifact("if_demo_plot.png")

    print("✅ Modelo Isolation Forest logado no MLflow com sucesso.")