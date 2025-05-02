# Autor: Francisco J. Becerra
# Fecha: 02/05/2025
# Curso: UMA - Python para principiantes
# Tema: 3
# Ejercicio: 06-Ejercicio-1.py

# Condición previa:
'''
NINGUNA
'''

# Descripción:
'''
Utilizar find() y los slices (:) para extraer el número en un
string como el que aparece a continuación. Convertir el
número a flotante y mostrarlo.
¡Ojo! No asumir que el número es 0.8475, es solo un
ejemplo. No sabemos qué número es, tenemos que
extraerlo. Sí podemos suponer que el resto de la línea es
igual. Esto es, comienza por "X-DSPAM-Confidence..."
"X-DSPAM-Confidence: 0.8475"
'''

# Variables
separador = ":"
posSeparador = -1
longStrEntrada = 0
valorTest = "test"
formatoRequerido ="Texto: numeroDecimal"

def devolverSubcadena(strEntrada):
	posSeparador = strEntrada.find(separador)
	#Cortamos la cadena y suprimimos espacios
	strEntrada = strEntrada[posSeparador+1:len(strEntrada)].strip()
	
	return strEntrada

def comprobarValorNumerico(strEntrada):		
	try:
		valorNumerico = float(strEntrada)
		print("Valor numerico: "+str(valorNumerico))
	except:
		print('[ERR] La cadena no contenia valor numerico')
		print('[ERR] Formato Requerido => '+formatoRequerido)

# Main
strEntrada = input('Introduzca dato [escriba Test para prueba automatica]: ')

# Test
if strEntrada.upper()==valorTest.upper():
	strEntrada = "X-DSPAM-Confidence: 0.8475"

print('Cadena entrada: '+strEntrada)
posSeparador = strEntrada.find(separador)

if posSeparador == -1:
	print(' [ERR] Formato de entrada Erroneo')
	print(' [ERR] Formato Requerido => '+formatoRequerido)
else:
	strEntrada = devolverSubcadena(strEntrada)	
	comprobarValorNumerico(strEntrada)
	
