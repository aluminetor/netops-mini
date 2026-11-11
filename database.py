import sqlite3

conexion = sqlite3.connect("netops.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sede TEXT NOT NULL,
        tipo TEXT NOT NULL,
        latencia_ms INTEGER NOT NULL,
        prioridad TEXT NOT NULL,
        estado TEXT NOT NULL
    )
""")

conexion.commit()
conexion.close()