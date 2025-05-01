# Autor: Francisco J. Becerra
# Fecha: 01/05/2025
# Curso: UMA - Python para principiantes
# Tema: 2
# Ejercicio: 05-Ejercicio.py

# Condición previa:
'''
NINGUNA
'''

# Descripción:
'''
Escribe un programa que pida números al usuario hasta
que escriba 'fin'. Una vez escrito 'fin', el programa debe
mostrar el número más grande y el más pequeño. Si el
usuario escribe algo diferente a un número, se debe
capturar con un try/except e ignorar el valor introducido.
Probar con 7, 2, bob, 10, y 4
Nota: el ejercicio debe resolverse con los visto hasta el
momento. No está permitido el uso de otros elementos
como listas (que se verán posteriormente)
'''

# Variables
numMax = 0
numMin = 0
contadorNum = 0
nuevoValor = ''
valorSalida ='fin'

def comprobarAsignarMayor(nuevoValor):
	if nuevoValor > numMax:
		numMax = nuevoValor
	
def comprobarAsignarMenor(nuevoValor):
	if nuevoValor < numMin:
		numMin = nuevoValor
		
while nuevoValor !==valorSalida :
	try:
		nuevoValor = input('Introduzca un numero [fin para termina]:  '))		
		comprobarAsignarMayor(float(nuevoValor))
		comprobarAsignarMenor(float(nuevoValor))	
		
	except:
		

	
	
			
