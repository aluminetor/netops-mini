# NetOps Mini

NetOps Mini es un proyecto práctico en Python para simular el monitoreo de conectividad de varias sedes y gestionar incidentes de latencia. Una API FastAPI entrega métricas simuladas, un cliente genera tickets en SQLite y un dashboard Streamlit permite revisar y cerrar incidentes.

El proyecto sirve como práctica de automatización de redes, APIs REST, SQL y visualización de indicadores operativos.

## Cómo funciona

```text
API FastAPI → cliente Python → SQLite ↔ dashboard Streamlit
```

| Archivo | Función |
| --- | --- |
| `main.py` | Expone las métricas simuladas en `GET /sedes` y un mensaje de bienvenida en `GET /saludo`. |
| `cliente.py` | Consulta la API una vez por ejecución, aplica los umbrales y registra los tickets nuevos. |
| `database.py` | Crea la tabla de tickets y contiene las operaciones para guardar, comprobar y cerrar incidentes. |
| `dashboard.py` | Muestra el total de tickets, la latencia media de los incidentes, el total de prioridad alta, un gráfico por prioridad y la tabla de incidentes. Permite cerrar tickets abiertos. |
| `consultar.py` | Lista tickets y muestra su latencia media y el total en consola. Al ejecutarse, primero intenta cerrar el ticket con ID 1. |
| `netops.db` | Almacena los tickets abiertos y cerrados. Los scripts usan este archivo desde el directorio de trabajo. |

La detección usa umbrales fijos de latencia. La API también devuelve la pérdida de paquetes como dato informativo.

| Latencia | Resultado |
| --- | --- |
| Hasta 100 ms | Sin ticket |
| Más de 100 ms y hasta 150 ms | Prioridad Media |
| Más de 150 ms | Prioridad Alta |

Cada incidente se registra como **Latencia elevada** con estado **Abierto**. En ejecuciones sucesivas, el cliente comprueba si existe un ticket abierto del mismo tipo para la misma sede antes de crear otro. El cierre es manual y el ticket cerrado queda en el historial.

## Instalación

Necesitas Python 3 con `pip`. Desde la raíz del proyecto, ejecuta en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install fastapi uvicorn requests streamlit pandas
```

SQLite está incluido en la biblioteca estándar de Python.

## Uso

1. Inicia la API desde la raíz del proyecto y deja la terminal abierta.

   ```powershell
   python -m uvicorn main:app --reload
   ```

   Puedes consultar la [documentación interactiva de la API](http://127.0.0.1:8000/docs) o ver directamente las [métricas simuladas](http://127.0.0.1:8000/sedes).

2. En otra terminal, desde la misma carpeta y con el entorno virtual activo, ejecuta el cliente. Este prepara la tabla `tickets` si todavía no existe.

   ```powershell
   python cliente.py
   ```

3. Abre el dashboard desde esa misma carpeta.

   ```powershell
   python -m streamlit run dashboard.py
   ```

   Abre la URL que muestra Streamlit. En **Gestión de tickets**, selecciona el ID de un ticket abierto y pulsa **Cerrar ticket**. El estado cambia a **Cerrado** en la tabla.

## Prueba manual de integración

Con la API y el dashboard en ejecución, comprueba el ciclo con los datos simulados. Bogotá tiene una latencia de 135 ms y es la única sede que supera el umbral.

1. Ejecuta `python cliente.py`. Si ya existe un ticket abierto de Bogotá, puedes usarlo como punto de partida. En caso contrario, debe aparecer uno de **Prioridad Media**.
2. Ejecuta el cliente otra vez. La salida esperada es `TICKETS: []`.
3. Cierra el ticket de Bogotá desde el dashboard y verifica que figure como **Cerrado**.
4. Ejecuta nuevamente el cliente y recarga el dashboard. Debe aparecer un ticket **Abierto** con un ID nuevo y el anterior debe seguir en el historial.
