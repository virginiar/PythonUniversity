# Actualizar registros desde Python a mysql

import os

import mysql.connector

personas_db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),  # 127.0.0.1
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database='personas_db'
)

# Ejecutar la sentencia update
cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s;'
valores = ('Victoria', 'Flores', 45, 3)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la información...')
cursor.close()
personas_db.close()
