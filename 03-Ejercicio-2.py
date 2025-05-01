# Autor: Francisco J. Becerra
# Fecha: 01/05/2025
# Curso: UMA - Python para principiantes
# Tema: 2
# Ejercicio: 03-Ejercicio-2.py

# Condición previa:
'''
Ejercicio: 03-Ejercicio-1
'''

# Descripción:
'''
Reescribe el programa de pagos usando try y except para
que se manejen adecuadamente entradas no numéricas
(nota: no hace falta quese vuelvan a pedir los números si falla)
	Introduzca las horas: 20
	Introduzca el precio/hora: nueve
	Error, por favor introduzca un número
	Introduzca las horas: cuarenta
	Error, por favor introduzca un número
'''

# Variables
numHoras = 0
precioHora = 0
horasJornadaNormal = 40
totalJornadaNormal = 0

calculoHoraExtra = 1.5
numHorasExtras = 0
precioHoraExtra = 0
totalJornadaExtra = 0

# Introducir datos con conversion
print('------------------------')
print('Calculo de Total a Pagar')
print('------------------------')
try:
	numHoras = float(input('Introduzca las horas: '))
	precioHora = float(input('Introduzca el precio/hora: '))

	# Calculos
	# Comprobar si el tiempo supera la jornada normal para calcular extra
	if numHoras > horasJornadaNormal :
		numHorasExtras = numHoras - horasJornadaNormal 
		numHoras = numHoras - numHorasExtras	
		precioHoraExtra = calculoHoraExtra * precioHora
		totalJornadaExtra = numHorasExtras * precioHoraExtra

	totalJornadaNormal = numHoras * precioHora	
		
	# Informacion Calculo
	print('-----------------------------------------------------------------')
	print('Horas: '+str(numHoras)+' - Pre. Hora: '+str(precioHora))

	if numHorasExtras > 0 :
		print('Horas Extras: '+str(numHorasExtras)+' - Pre. Hora Extra('+str(calculoHoraExtra)+'): '+str(precioHoraExtra))
		
	print('-----------')
	print('Horas: '+str(numHoras+numHorasExtras))

	# Totales
	if numHorasExtras > 0 :
		print('Total: '+str(totalJornadaNormal+totalJornadaExtra))	
	else :		
		print('Total: '+str(totalJornadaNormal))

	# Informacion Desglose
	if numHorasExtras > 0 :
		print('Desglose : ')
		print('-----------')
		print('H. Normales: '+str(numHoras)+' - Total H. Normales: '+str(totalJornadaNormal))
		print('H. Extras: '+str(numHorasExtras)+' - Total H. Extras: '+str(totalJornadaExtra))

except:
	print('Error, por favor introduzca un número')		
