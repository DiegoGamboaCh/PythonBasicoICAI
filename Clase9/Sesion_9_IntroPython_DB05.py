""" CASO: BORRADO Y ACTUALIZADO EN DB
"""

""" Importar el módulo de acceso a nuestra DB, en este caso MySql  y el datetime
"""
import mysql.connector as db

from datetime import datetime

"""
Llamamos a la función connect pasando la ubicación de nuestro servidor que es 'localhost'
    - el  usuario que por defecto al instalar MySQL es el usuario 'root'
    - la clave de ese usuario que tiene por defecto es un string vacío
"""
miconexion = db.connect(host="localhost",user="root",passwd="",  database="sakila")

"""
El método "cursor" en Python permite que el código ejecute un comando SQL  en una sesión de base de datos.
Los cursores se crean con el método "connection.cursor()" y están vinculados a la conexión mientras esta exista 
"""
micursor = miconexion.cursor()


"""
Por medio del método "execute" vamos a poder pasar instrucciones SQL a la BD
- En este caso se va a borrar   filas a una tabla 
"""

ID = 201
dato = ("Brad", "Pitt")

# preparamos el estatuto de borrado
sql_delete = f"DELETE FROM  actor WHERE actor_id = {ID}"
# preparamos el estatuto de actualización
sql_update = "UPDATE actor SET first_name=%s WHERE last_name= %s"

"""
 Se invoca al método 'execute' y le pasamos los sql
"""

micursor.execute(sql_delete)
micursor.execute(sql_update,dato)



"""
 Usamos el método 'commit' para confirmar de forma permanente un conjunto de cambios provisionales antes realizados
"""
miconexion.commit()


"""
Por medio del método "close" cerramos la conexión a la DB
"""
miconexion.close()
