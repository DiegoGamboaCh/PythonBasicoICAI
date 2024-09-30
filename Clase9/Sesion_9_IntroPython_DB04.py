""" CASO: INSERCIÓN EN DB
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
- En este caso se va a verifica cual es la cantidad de elementos en la tabla , para luego ser usada como indice
"""

micursor.execute('select  max(actor_id) from actor')
""" Se  obtiene el primer resultado por medio del método fetchone()
 - este método obtiene la siguiente fila (caso) del conjunto de datos activo
 """
resultado = micursor.fetchone()
ID  = 1
if resultado:
    primer_valor = resultado[0]  # Accede al primer valor de la fila
    ID = primer_valor + 1


"""
Por medio del método "execute" vamos a poder pasar instrucciones SQL a la BD
- En este caso se va a insertar una fila a una tabla 
- Por medio de un string con el comando SQL insert disponiendo la máscara %s donde queremos que se sustituya por un valor que le pasaremos al método execute
"""


sql = "INSERT INTO actor(actor_id, first_name, last_name, last_update) VALUES (%s,%s,%s,%s)"

"""
La variable dato es una tupla que contiene los datos que se utilizarán en la sustitución %s:
"""
dato = (ID, 'TOMAS', 'CRUZ', datetime.now())

"""
 Se invoca al método 'execute' y le pasamos las dos variables que acabamos de crear
"""
micursor.execute(sql,dato)


"""
Se insertan más datos 
"""
ID += 1
dato = (ID, 'RAMON', 'VALDEZ', datetime.now())
micursor.execute(sql,dato)
ID += 1
dato = (ID, 'FELIPE', 'PITT', datetime.now())
micursor.execute(sql,dato)
ID += 1
dato = (ID, 'JUAN', 'DICAPRIO', datetime.now())
micursor.execute(sql,dato)

"""
 Usamos el método 'commit' para confirmar de forma permanente un conjunto de cambios provisionales antes realizados
"""
miconexion.commit()






"""
Por medio del método "close" cerramos la conexión a la DB
"""
miconexion.close()
