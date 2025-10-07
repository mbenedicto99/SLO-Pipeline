# Finalidade : Coleta de SLOs do PostgreSQL
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# fetch_slos.py
import psycopg2
import pandas as pd

def fetch_slos_from_postgres():
    conn = psycopg2.connect(
        dbname="your_db",
        user="your_user",
        password="your_pass",
        host="your_host",
        port="5432"
    )
    query = "SELECT * FROM slo_definitions;"
    return pd.read_sql(query, conn)
