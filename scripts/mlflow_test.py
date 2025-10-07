# mlflow_test.py
import mlflow
import mlflow.sklearn
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_blobs

# 👉 Aponta para o experimento "O11y"
mlflow.set_experiment("O11y")

with mlflow.start_run():
    mlflow.set_tag("author", "mlops-test")

    # Dataset fake
    X, _ = make_blobs(n_samples=100, centers=1, cluster_std=0.5, random_state=42)

    # Treina modelo
    model = IsolationForest(n_estimators=100, contamination=0.05)
    model.fit(X)

    # Loga parâmetros e modelo
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("contamination", 0.05)
    mlflow.sklearn.log_model(model, "model")

    print("✔ Run logado com sucesso!")
