# Finalidade : Deploy com MLflow
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# deploy_model.py
import mlflow
import mlflow.sklearn
import joblib

def deploy_model(model_path="model.pkl"):
    model = joblib.load(model_path)
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, "model")
        print("Model logged to MLflow.")
