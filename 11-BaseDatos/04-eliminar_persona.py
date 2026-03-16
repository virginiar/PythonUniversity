# Eliminar registros desde Python a mysql

import os

import mysql.connector

personas_db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),  # 127.0.0.1
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database='personas_db'
)

# Ejecutar la sentencia delete
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (3,)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha eliminado el registro')
cursor.close()
personas_db.close()
