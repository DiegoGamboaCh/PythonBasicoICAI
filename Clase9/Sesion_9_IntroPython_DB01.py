""" CASO: LISTADO DE  DB
"""


""" Importar el módulo de acceso a nuestra DB, en este caso MySql 
"""
import mysql.connector as db

"""
Llamamos a la función connect pasando la ubicación de nuestro servidor que es 'localhost'
    - el  usuario que por defecto al instalar MySQL es el usuario 'root'
    - la clave de ese usuario que tiene por defecto es un string vacío
"""
miconexion = db.connect(host="localhost",user="root",passwd="")

"""
El método "cursor" en Python permite que el código ejecute un comando SQL  en una sesión de base de datos.
Los cursores se crean con el método "connection.cursor()" y están vinculados a la conexión mientras esta exista 
"""
micursor = miconexion.cursor()
"""
Por medio del método "execute" vamos a poder pasar instrucciones SQL a la BD
- En este caso se va a retornar las bases de datos y desplegar las mismas
"""
micursor.execute('show databases')
for db in micursor:
    print(db)

"""
Por medio del método "close" cerramos la conexión a la DB
"""
miconexion.close()
