import sqlite3


def crear_tabla():
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

def guardar_ticket(ticket):
    conexion = sqlite3.connect("netops.db")
    cursor = conexion.cursor()

    cursor.execute(
        """INSERT INTO tickets
        (sede, tipo, latencia_ms, prioridad, estado)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            ticket["sede"],
            ticket['tipo'],
            ticket['latencia_ms'],
            ticket['prioridad'],
            ticket['estado']
        ),
    )
    
    conexion.commit()
    conexion.close()
