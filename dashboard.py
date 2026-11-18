import sqlite3
import streamlit as st
import pandas as pd 
from database import cerrar_ticket
conexion = sqlite3.connect("netops.db")
cursor = conexion.cursor()

st.title("NetOps Mini")
st.write("Dashboard de monitoreo de incidentes")

#python -m streamlit run dashboard.py

cursor.execute("SELECT COUNT(*) FROM tickets")
cantidad_tickets = cursor.fetchone()[0]

cursor.execute(
    "SELECT COALESCE(AVG(latencia_ms), 0) FROM tickets"
)

promedio_latencia = cursor.fetchone()[0]


cursor.execute(
    "SELECT COUNT(*) FROM tickets WHERE prioridad = ?",
    ("Prioridad Alta",)
)
count_alta = cursor.fetchone()[0]


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tickets registrados", cantidad_tickets)

with col2:
    st.metric("Latencia media", f"{promedio_latencia:.2f} ms")

with col3:
    st.metric("Prioridad alta", count_alta)

cursor.execute("SELECT * FROM tickets")
tickets = cursor.fetchall()
conexion.close()

df = pd.DataFrame(
    tickets,
    columns=[
        "ID",
        "Sede",
        "Tipo",
        "Latencia (ms)",
        "Prioridad",
        "Estado"
    ]
)

conteo = df["Prioridad"].value_counts()

st.subheader("Tickets por prioridad")

if not df.empty:
    st.bar_chart(conteo)
else:
    st.info("Todavía no hay incidentes registrados.")

st.subheader("Incidentes registrados")
st.dataframe(df, use_container_width=True)

st.subheader("Gestión de tickets")

tickets_abiertos = df[df["Estado"] == "Abierto"]

if not tickets_abiertos.empty:
    ticket_id = st.selectbox(
        "Selecciona un ticket abierto",
        options=tickets_abiertos["ID"],
        key="ticket_abierto"
    )

    if st.button("Cerrar ticket", key="cerrar_ticket"):
        cerrar_ticket(int(ticket_id))
        st.toast("Ticket cerrado correctamente")
        st.rerun()
else:
    st.info("No hay tickets abiertos.")
