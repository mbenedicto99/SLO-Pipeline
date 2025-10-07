# test_isolation_forest_complex.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_moons, make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

print("✅ Bibliotecas importadas com sucesso!")

# Gerar dados não lineares com ruído + dados mistos
X1, _ = make_moons(n_samples=3000, noise=0.15, random_state=142)
X2, _ = make_classification(n_samples=2000, n_features=5, n_informative=3, n_redundant=0, random_state=142)

# Combinar e embaralhar
X_combined = np.vstack([X1, X2[:, :2]])
np.random.shuffle(X_combined)

# Padronizar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_combined)

# Reduzir para 2D para visualização
pca = PCA(n_components=2)
X_vis = pca.fit_transform(X_scaled)

# Treinar Isolation Forest
model = IsolationForest(n_estimators=150, contamination=0.1, random_state=42)
model.fit(X_scaled)
preds = model.predict(X_scaled)

# Visualizar
plt.figure(figsize=(8, 6))
plt.scatter(X_vis[:, 0], X_vis[:, 1], c=preds, cmap='coolwarm', edgecolors='k')
plt.title("Detecção de Anomalias com Isolation Forest - Dados Complexos")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("isolation_forest_complex_plot.png")
plt.show()

print("📊 Gráfico salvo como 'isolation_forest_complex_plot.png'")

# Log no MLflow
mlflow.set_experiment("IsolationForest_Complex")
with mlflow.start_run():
    mlflow.log_param("contamination", 0.1)
    mlflow.log_param("n_estimators", 150)
    mlflow.log_metric("num_anomalies", int((preds == -1).sum()))

    signature = infer_signature(X_scaled, preds)
    mlflow.sklearn.log_model(model, "model", signature=signature, input_example=X_scaled[:2])
    mlflow.log_artifact("isolation_forest_complex_plot.png")

    print("✅ Modelo e gráfico logados no MLflow com sucesso!")
