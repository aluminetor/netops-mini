from fastapi import FastAPI

app = FastAPI()
#.\.venv\Scripts\Activate.ps1
# python -m uvicorn main:app --reload
sedes = [
{
    "nombre":"Medellín",
    "latencia_ms":25,
    "perdida_paquetes": 0
},
{
    "nombre":"Bogotá",
    "latencia_ms":135,
    "perdida_paquetes": 0.08
},
{
    "nombre":"Barranquilla",
    "latencia_ms":42,
    "perdida_paquetes": 0.01
}
]

@app.get("/sedes")
def obtener_sedes():
    return sedes

@app.get("/saludo")
def saludar():
    return {"mensaje": "Bienvenido a NetOps Mini"}
# for sede in sedes:
#     print(f"{sede["nombre"]}: {sede["latencia_ms"]} ms")

