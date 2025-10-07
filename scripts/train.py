# Finalidade : Treinamento
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# train.py
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

def train():
    # Dados sintéticos (substitua pelos seus)
    df = pd.read_csv("data/data.csv")
    df = df.dropna()
    X = StandardScaler().fit_transform(df.select_dtypes(include="number"))

    with mlflow.start_run():
        model = IsolationForest(n_estimators=100, contamination=0.05)
        model.fit(X)

        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("contamination", 0.05)
        mlflow.sklearn.log_model(model, "model")

        joblib.dump(model, "models/model.pkl")
        print("Model trained and logged to MLflow")

if __name__ == "__main__":
    train()

