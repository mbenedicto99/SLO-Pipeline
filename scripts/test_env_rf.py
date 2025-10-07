# test_env_rf.py

import mlflow
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from mlflow.models.signature import infer_signature

print("✅ Bibliotecas importadas com sucesso!")

# Carregar dataset real
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("✅ Modelo Random Forest treinado com sucesso!")

# Avaliação e assinatura
accuracy = model.score(X_test, y_test)
signature = infer_signature(X_test, model.predict(X_test))
input_example = X_test.iloc[:2]

# Log no MLflow
mlflow.set_experiment("RandomForest_BreastCancer")
with mlflow.start_run():
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model", signature=signature, input_example=input_example)
    print(f"✅ Modelo logado no MLflow com accuracy={accuracy:.4f}")

# Plotar importância das features
importances = model.feature_importances_
features = X.columns
indices = importances.argsort()[::-1]

plt.figure(figsize=(10, 6))
plt.title("Importância das Features - Random Forest")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), features[indices], rotation=90)
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.show()

print("📊 Gráfico salvo como 'feature_importance.png'")