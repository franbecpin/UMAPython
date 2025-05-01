# Autor: Francisco J. Becerra
# Fecha: 2704/2025
# Curso: UMA - Python para principiantes
# Tema: 2
# Ejercicio: 1

# Condición previa:
'''
Escribir un programa que pregunte al usuario
un número de horas y el precio por hora para
calcular el total a pagar.
Introduzca las horas: 35
Introduzca el precio/hora: 2.75
Total: 96.25
'''

# Descripción:
'''
Reescribe el programa de pagos para incrementar en un
factor de 1.5 las horas que se trabajen por encima de 40
horas (hasta 40 horas todas se cobran a precio normal)
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
