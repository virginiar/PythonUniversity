# Seleccionar registros desde Python a mysql
import os

import mysql.connector

personas_db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),  # 127.0.0.1
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database='personas_db'
)

# Ejecutar la sentencia select
cursor = personas_db.cursor()
cursor.execute('SELECT * FROM personas;')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)
cursor.close()
personas_db.close()
