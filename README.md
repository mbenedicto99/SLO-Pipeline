
# 🧠 MLOps Pipeline - Análise de Anomalias orientado a SLOs

Este projeto implementa um pipeline completo de MLOps para **detecção de anomalias em ambientes de nuvem**, orientado por **SLOs (Service Level Objectives)**. O objetivo é garantir a confiabilidade de sistemas distribuídos com monitoramento contínuo, alertas automáticos, e retraining de modelos com base em violações de SLOs.

---

## 📌 Componentes do Pipeline

- 🔍 Coleta de métricas da cloud (ex: Prometheus)
- 📦 Armazenamento de dados em data lake
- 🧼 Pré-processamento com limpeza e normalização
- 🎯 Análise e validação com base em SLOs (PostgreSQL)
- 🧠 Treinamento com Isolation Forest (modelo de anomalia)
- 🚀 Deploy com MLflow Tracking e Serving
- 📈 Monitoramento em tempo real
- 🔁 Recalibração automática com novo treinamento
- 🚨 Alertas via Alertmanager
- 👤 Interface para ajuste de SLOs com Streamlit

---

## 🧰 Requisitos

- Python 3.9+
- PostgreSQL
- Prometheus + Alertmanager
- MLflow
- Virtualenv ou Conda

---

## 🛠️ Setup do Projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/slo-mlops-pipeline.git
cd slo-mlops-pipeline

# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Inicie o MLflow Tracking UI (em outra aba)
mlflow ui
```

---

## ⚙️ Execução

```bash
# Executar pipeline completo (exemplo)
python scripts/mlflow_test.py

# Ou usar MLflow project
mlflow run .
```

---

## 🗺️ Diagrama Mermaid

```mermaid
graph TD
  A[Coleta de métricas da cloud]
  B[Armazenamento em data lake]
  C[Pré-processamento de dados]
  D[Análise orientada a SLOs]
  E[Treinamento de modelo de detecção de anomalias]
  F[Validação baseada em SLOs]
  G[Deploy do modelo em ambiente cloud]
  H[Monitoramento em tempo real]
  I[Recalibração automática (retraining)]
  J[Alerta e resposta a incidentes]
  K[Ajuste de SLOs com base em feedback]

  A --> B --> C --> D --> E --> F --> G --> H
  H --> I --> E
  H --> J --> K --> D
```

---

## 🖼️ Diagrama Ilustrado

> Representação visual do pipeline completo de MLOps orientado a SLOs:

![Pipeline MLOps](./MLOps-SLO.png)

---

## 🧪 Ferramentas utilizadas

- **Python**
- **scikit-learn**
- **MLflow**
- **Prometheus / Alertmanager**
- **PostgreSQL**
- **Streamlit**

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
