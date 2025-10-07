# Finalidade : Interface Streamlit para atualização de SLOs
# Autor : Marcos de Benedicto
# Data : 07/10/2025

# update_slo_ui.py
import streamlit as st
import psycopg2

def update_slo(slo_name, target_value):
    conn = psycopg2.connect(dbname="your_db", user="your_user", password="your_pass", host="your_host")
    cur = conn.cursor()
    cur.execute("UPDATE slo_definitions SET target=%s WHERE name=%s", (target_value, slo_name))
    conn.commit()
    st.success("SLO updated!")

st.title("Atualização de SLOs")
slo_name = st.text_input("Nome do SLO")
target = st.number_input("Novo alvo", min_value=0.0, max_value=1.0, step=0.01)

if st.button("Atualizar SLO"):
    update_slo(slo_name, target)
