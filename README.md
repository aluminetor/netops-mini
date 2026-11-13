# NetOps Mini

Sistema ligero de monitoreo de red y gestión de incidentes construido con **FastAPI**, **SQLite** y **Streamlit**. Simula la consulta de métricas de conectividad por sede, genera tickets automáticos ante latencias elevadas evitando duplicados abiertos y visualiza los incidentes en un dashboard interactivo.

## Características

- **API REST de sedes**: Expone métricas simuladas de latencia y pérdida de paquetes por sede (`main.py`).
- **Cliente de monitoreo y generación de tickets**: Consulta la API y registra incidentes en SQLite según umbrales de latencia (`cliente.py`).
- **Prevención de duplicados**: Verifica si ya existe un ticket abierto para la misma sede y tipo antes de insertar uno nuevo (`database.py`).
- **Consulta por consola**: Muestra todos los tickets registrados, el promedio de latencia y el total de incidentes (`consultar.py`).
- **Dashboard interactivo**: Visualiza métricas clave, gráfico de barras por prioridad y tabla de incidentes en Streamlit (`dashboard.py`).

## Estructura del proyecto

```text
netops-mini/
├── main.py          # API FastAPI con endpoints /sedes y /saludo
├── database.py      # Funciones de acceso y creación de tabla en SQLite (netops.db)
├── cliente.py       # Script cliente que consulta /sedes y crea tickets en la BD
├── consultar.py     # Script de consulta rápida de tickets y métricas por consola
├── dashboard.py     # Dashboard web en Streamlit
├── .env.example     # Ejemplo de variable de entorno (DATABASE_PATH)
└── .gitignore       # Exclusiones de Git (.env, .venv/, __pycache__/, *.py[cod])
```
