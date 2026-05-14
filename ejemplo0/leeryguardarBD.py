"""
    Script para leer y guardar datos en la base de datos
    Lee datos del CSV y los guarda en la base de datos
"""

import csv
import os
from base_datos import conn

# Obtener la ruta del directorio donde está el script
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(script_dir, 'data', 'info.csv')

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.
cursor = conn.cursor()

print("=" * 60)
print("LEYENDO DATOS DEL ARCHIVO CSV")
print("=" * 60)

# Leer datos del archivo CSV
datos_a_guardar = []
try:
    with open(ruta_csv, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        # Saltar la primera línea (encabezados)
        next(lector_csv)
        # Leer cada fila del CSV
        for fila in lector_csv:
            nombre, apellido, cedula, edad = fila
            datos_a_guardar.append((nombre, apellido, cedula, int(edad)))
    print(f"✓ Se leyeron {len(datos_a_guardar)} registros del CSV\n")
except FileNotFoundError:
    print(f"✗ Error: No se encontró el archivo {ruta_csv}")
    cursor.close()
    exit()

print("=" * 60)
print("GUARDANDO DATOS EN LA BASE DE DATOS")
print("=" * 60)

# Guardar cada registro en la base de datos
for nombre, apellido, cedula, edad in datos_a_guardar:
    cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)
    
    try:
        cursor.execute(cadena_sql)
        print(f"Guardado: {nombre} {apellido}")
    except Exception as e:
        print(f"Error al guardar {nombre}: {e}")

# confirmar los cambios a través del objeto importado de tipo Connection
conn.commit()

print("\n" + "=" * 60)
print("LEYENDO DATOS DE LA BASE DE DATOS")
print("=" * 60 + "\n")

# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)

# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# Mostrar cantidad de registros
print(f"Total de registros: {len(informacion)}\n")

# se realiza un ciclo repetitivo para recorrer la secuencia de información resultante
print(f"{'ID':<5} {'NOMBRE':<20} {'APELLIDO':<20} {'CÉDULA':<15} {'EDAD':<5}")
print("-" * 65)

for d in informacion:
    print(f"{d[0]:<5} {d[1]:<20} {d[2]:<20} {d[3]:<15} {d[4]:<5}")

print("-" * 65)

# cerrar el enlace a la base de datos (recomendado)
cursor.close()

print("\n¡Proceso completado exitosamente!")
