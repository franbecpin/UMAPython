# Autor: Francisco J. Becerra
# Fecha: 03/05/2025
# Curso: UMA - Python para principiantes
# Tema: 3
# Ejercicio: 07-Ejercicio.py

# Condición previa:
'''
Requiere el fichero
- mbox-short.txt
'''

# Descripción:
'''
Escribir un programa que pregunte por un
nombre de archivo, lo abra, y lo lea mostrando
las líneas de la forma:
X-DSPAM-Confidence: 0.8475
Contar las líneas y extraer los valores flotantes de
cada una de ellas, calculando el promedio y
mostrándolo al final.
Se pueden descargar datos de muestra desde el
archivo mbox-short.txt en Campus Virtual. El
valor promedio resultante debería ser:
0.7507185185185187
'''

# Variables
nomFichero=''
fichero = None
valorFiltro = 'X-DSPAM-Confidence:'
	
def procesarLineasFichero(fichero):
	contadorLineas = 0
	sumaLineas = 0
	
	for linea in fichero :
		if linea.startswith(valorFiltro)==True:							
			valorLinea = linea[linea.find(':')+2:len(linea)]			
			valorLinea = valorLinea.rstrip()
			
			#Filtramos los numeros por el separador decimal
			#Por si alguna linea presenta valor no decimal 
			if valorLinea.find('.')!=-1 :						
				try:
					numero = float(valorLinea)					
					sumaLineas = sumaLineas + float(numero)
					contadorLineas = contadorLineas + 1
				except:					
					pass	
									
	print('Lineas computadas: '+str(contadorLineas))					
	print('Suma: '+str(sumaLineas))	
	print('--------------')
	print('Promedio: '+str(sumaLineas/contadorLineas))
		
			
# Main
nomFichero = input('Introduzca nombre del fichero: ')

try:
	fichero = open(nomFichero, 'r')
	print('[OK] Abierto fichero: '+nomFichero)		
	procesarLineasFichero(fichero)		
	
except:
	print('[ERR] No se encontro el fichero: '+nomFichero)	


try:
	fichero.close()
	print('[OK] Cerrado Fichero: '+nomFichero)
except:
	print('[ERR] No se pudo cerrar el fichero: '+nomFichero)
