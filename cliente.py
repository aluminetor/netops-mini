import requests

url = "http://127.0.0.1:8000/sedes"

respuesta = requests.get(url, timeout=5)
respuesta.raise_for_status()

sedes = respuesta.json()

for sede in sedes:
    if sede["latencia_ms"] > 100:
        print(f"ALERTA: {sede['nombre']} presenta latencia de {sede['latencia_ms']} ms")