# Insertar registros desde Python a mysql

import os

import mysql.connector

personas_db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),  # 127.0.0.1
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database='personas_db'
)

# Ejecutar la sentencia insert
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s);'
valores = ('Victor', 'Ramos', 46)
cursor.execute(sentencia_sql, valores)
personas_db.commit()  # Guardar los cambios en la base de datos
print(f'Se ha agregado el nuevo registro a la base de datos : {valores}')
cursor.close()
personas_db.close()
