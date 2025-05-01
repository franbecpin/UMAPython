# Autor: Francisco J. Becerra
# Fecha: 01/05/2025
# Curso: UMA - Python para principiantes
# Tema: 2
# Ejercicio: 04-Ejercicio.py

# Condición previa:
'''
Ejercicio: 03-Ejercicio-1
Ejercicio: 03-Ejercicio-2
'''

# Descripción:
'''
Reescribe el cálculo del pago por horas de la unidad
anterior y escribe una función llamada calculapago
que toma dos parámetros (horas y precio) y retorna
el total a pagar.
	Introduzca las horas: 45
	Introduzca el precio/hora: 10
	Total: 475.0
	475 = 40 * 10 + 5 * 15

Es decir, debes definir una función con la siguiente
cabecera:
	def calculapago(horas,precio_hora):
La función realizará el cálculo del total a pagar y
acabará retornando el pago total con return
Desde fuera de la función, deberías poder hacer algo
así como:
	print(calculapago(horas,precio_hora))
'''

# Variables
numHoras = 0
precioHora = 0
horasJornadaNormal = 40

def calculapago(numHoras,precioHora):		
	totalJornadaNormal = 0
	calculoHoraExtra = 1.5
	numHorasExtras = 0
	precioHoraExtra = 0
	totalJornadaExtra = 0
		
	# Calculos
	# Comprobar si el tiempo supera la jornada normal para calcular extra
	if numHoras > horasJornadaNormal :
		numHorasExtras = numHoras - horasJornadaNormal 
		numHoras = numHoras - numHorasExtras	
		precioHoraExtra = calculoHoraExtra * precioHora
		totalJornadaExtra = numHorasExtras * precioHoraExtra

	totalJornadaNormal = numHoras * precioHora	
	
	# Sumar horas extras al total
	if numHorasExtras > 0 :
		totalJornadaNormal 	= totalJornadaNormal + totalJornadaExtra	
		
	return totalJornadaNormal


# Introducir datos con conversion
print('------------------------')
print('Calculo de Total a Pagar')
print('------------------------')
try:
	numHoras = float(input('Introduzca las horas: '))
	precioHora = float(input('Introduzca el precio/hora: '))
	
	# Calcular el total desde la funcion
	print('Total: '+str(calculapago(numHoras,precioHora)))
	
	
except:
	print('Error, por favor introduzca un número')	

	
	
			
