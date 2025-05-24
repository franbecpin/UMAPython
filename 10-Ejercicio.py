# Autor: Francisco J. Becerra
# Fecha: 24/05/2025
# Curso: UMA - Python para principiantes
# Tema: 4
# Ejercicio: 10-Ejercicio.py

# Condición previa:
'''
Requiere el fichero
- mbox-short.txt
'''

# Descripción:
'''
Escribe un programa que lea el archivo mbox-short.txt y
muestre la distribución por horas del día de los
mensajes.
Se puede extraer la hora de las líneas que comiencen
por 'From ', extrayendo la hora completa y dividiendo
una segunda vez con los ':' como delimitador.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16
2008
Una vez hayas obtenido el total de mensajes en cada
hora, muestra los totales ordenados por hora. Deberías
obtener el resultado que se muestra a la derecha

04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

# Variables
nomFichero=''
fichero = None
valorBusqueda = 'From'
valorExclusion = 'From:'

def leerLineas(fichero):
	direcciones = list()
	incluidos = 0
	excluidos = 0
	
	for linea in fichero:
		if linea.startswith(valorBusqueda) :
			if linea.split()[0] != valorExclusion:
				incluidos = incluidos + 1
				direcciones.append(linea.split())
				#print (linea.split())
			else:
				excluidos = excluidos +1	
				
	calcularHoras(direcciones)			
		
	
def calcularHoras(direcciones):
	horas = dict()
	
	for direccion in direcciones:
		#Cortar hora
		hora = direccion[5] # Posición de la hora en la direccióm
		hora = hora[0: hora.find(':')]
				
		horas[hora] = horas.get(hora, 0) +1
		
	 
	for key,valor in sorted(horas.items()):
		print(key+" "+str(valor))	
		
	
# - Main -
nomFichero = input('Introduzca nombre del fichero: ')
# Test
#nomFichero = "datos/mbox-short.txt"

try:
	fichero = open(nomFichero, 'r')
	print('[OK] Abierto fichero: '+nomFichero)		
	leerLineas(fichero)		
	
except:
	print('[ERR] No se encontro el fichero: '+nomFichero)	


try:
	fichero.close()
	print('[OK] Cerrado Fichero: '+nomFichero)
except:
	print('[ERR] No se pudo cerrar el fichero: '+nomFichero)
