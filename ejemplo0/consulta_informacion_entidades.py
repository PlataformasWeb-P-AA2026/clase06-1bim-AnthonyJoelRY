"""
    Consulta de información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, apellido, cedula, edad
nombre = "Andrés Vinicio"
apellido = "Jara Vinces"
cedula = "1011019091"
edad = 30
cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

# ejecutar el SQL
cursor.execute(cadena_sql)

# nuevo registo
nombre = "Ana Salas"
cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)
cursor.execute(cadena_sql)

# nuevo registo
nombre = "Marco Barcia"
cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)
cursor.execute(cadena_sql)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()
print(informacion)
# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    print("%s - %s - %s - %s - %d" % (d[0], d[1], d[2], d[3], d[4]))

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
