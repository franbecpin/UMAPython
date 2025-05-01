# Autor: Francisco J. Becerra
# Fecha: 26/04/2025
# Curso: UMA - Python para principiantes
# Tema: 1
# Ejercicio: 02-Ejercicio

# Descripción:
'''
Escribir un programa que pregunte al usuario
un número de horas y el precio por hora para
calcular el total a pagar.
Introduzca las horas: 35
Introduzca el precio/hora: 2.75
Total: 96.25
'''

# Variables
numHoras = 0
precioHora = 0

# Introducir datos con conversion
print('------------------------')
print('Calculo de Total a Pagar')
print('------------------------')
numHoras = float(input('Introduzca las horas: '))
precioHora = float(input('Introduzca el precio/hora: '))


# Salida con conversion
print('-----------')
print('Total: '+str(numHoras*precioHora))
