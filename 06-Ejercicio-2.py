# Autor: Francisco J. Becerra
# Fecha: 02/05/2025
# Curso: UMA - Python para principiantes
# Tema: 3
# Ejercicio: 06-Ejercicio-2.py

# Condición previa:
'''
NINGUNA
'''

# Descripción:
'''
Pedir un nombre al Usuario de la forma:
NOMBRE APELLIDO1 APELLIDO2
Por ejemplo: José García Pérez
Dar la Vuelta al nombre y presentarlo en el formato:
APELLIDO1 APELLIDO2, NOMBRE
Por ejemplo: García Pérez, José
'''

# Variables
nomEntrada = input('Introduzca el nombre [nom app1 app2]: ')

#Asegurar no espacios delante o detras
nomEntrada = nomEntrada.strip()

# Localizar la posición del nombre
nomSalida = nomEntrada[nomEntrada.find(' '):len(nomEntrada)]+', '+nomEntrada[0:nomEntrada.find(' ')]
print('Apellidos, Nombre: '+nomSalida)



