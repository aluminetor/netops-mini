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

## Requisitos e instalación

- **Python 3**
- Dependencias utilizadas por los módulos del proyecto:
  - `fastapi`
  - `uvicorn`
  - `requests`
  - `streamlit`
  - `pandas`

### Configuración del entorno

1. Clona el repositorio y entra al directorio del proyecto:

   ```powershell
   git clone https://github.com/aluminetor/netops-mini.git
   cd netops-mini
   ```

2. Crea y activa el entorno virtual (en Windows PowerShell):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instala las dependencias necesarias:

   ```powershell
   pip install fastapi uvicorn requests streamlit pandas
   ```

4. Opcionalmente, copia el archivo de ejemplo `.env.example` a `.env` para referencia de configuración:

   ```powershell
   Copy-Item .env.example .env
   ```

   Contenido de `.env.example`:

   ```env
   DATABASE_PATH=netops.db
   ```

## Uso

### 1. Iniciar la API de sedes

Ejecuta el servidor FastAPI con Uvicorn:

```powershell
python -m uvicorn main:app --reload
```

Endpoints disponibles en `http://127.0.0.1:8000`:

- `GET /saludo`: Devuelve un mensaje de bienvenida (`{"mensaje": "Bienvenido a NetOps Mini"}`).
- `GET /sedes`: Devuelve la lista de sedes con sus métricas (`nombre`, `latencia_ms`, `perdida_paquetes`).

### 2. Ejecutar el cliente de monitoreo

Con la API en ejecución, corre el cliente para consultar `/sedes` y registrar incidentes en `netops.db`:

```powershell
python cliente.py
```

### 3. Consultar tickets desde consola

Para listar los tickets almacenados, ver la latencia promedio y la cantidad total de tickets:

```powershell
python consultar.py
```

### 4. Abrir el dashboard en Streamlit

Inicia la interfaz web para visualizar métricas, gráfico de barras por prioridad y la tabla de incidentes:

```powershell
python -m streamlit run dashboard.py
```
