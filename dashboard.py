import sqlite3
import streamlit as st

conexion = sqlite3.connect("netops.db")
cursor = conexion.cursor()

st.title("NetOps Mini")
st.write("Dashboard de monitoreo de incidentes")

#python -m streamlit run dashboard.py

cursor.execute("SELECT COUNT(*) FROM tickets")
cantidad_tickets = cursor.fetchone()[0]

st.metric("Tickets registrados", cantidad_tickets)


conexion.close()