import requests

url = "http://127.0.0.1:8000/sedes"

respuesta = requests.get(url, timeout=5)
respuesta.raise_for_status()

sedes = respuesta.json()
tickets = []

def crear_ticket(sede, prioridad):
    ticket = {
        "sede": sede["nombre"],
        "tipo": "Latencia elevada",
        "latencia_ms": sede["latencia_ms"],
        "prioridad": prioridad,
        "estado": "Abierto"
    }
    return ticket

for sede in sedes:
    latencia = sede['latencia_ms']

    if 100 < latencia <= 150:
        nuevo_ticket = crear_ticket(sede, "Prioridad Media")
    elif latencia > 150:
        nuevo_ticket = crear_ticket(sede, "Prioridad Alta")
    else:
        continue

    tickets.append(nuevo_ticket)

print(f"TICKETS: {tickets}")