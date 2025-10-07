# Finalidade : Pré-processamento de Dados
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# pre_process.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess(df):
    df_clean = df.dropna()
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_clean.select_dtypes(include='number'))
    return pd.DataFrame(df_scaled, columns=df_clean.select_dtypes(include='number').columns)
