import sqlite3

conexion = sqlite3.connect("netops.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM tickets")

tickets = cursor.fetchall()

for ticket in tickets:
    print(ticket)


cursor.execute("""
    SELECT AVG(latencia_ms)
    FROM tickets
""")

promedio = cursor.fetchone()[0]

print(f"Latencia promedio: {promedio:.2f} ms")


cursor.execute("""
    SELECT COUNT(*) FROM tickets
""")
cantidad_tickets = cursor.fetchone()[0]
print(f"Cantidad de tickets: {cantidad_tickets}")


conexion.close()