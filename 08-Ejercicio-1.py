# Autor: Francisco J. Becerra
# Fecha: 04/05/2025
# Curso: UMA - Python para principiantes
# Tema: 4
# Ejercicio: 08-Ejercicio-1.py

# Condición previa:
'''
Requiere el fichero
- romeo.txt
'''

# Descripción:
'''
Abre el archivo romeo.txt y léelo línea a línea.
Para cada línea, divide la línea en palabras
usando el método split(). El programa debería
construir una lista de palabras. Para cada palabra
de cada línea, comprobar si ya estaba en la lista,
y si no, añádela. Cuando el programa termine,
ordenar la lista y mostrar las palabras resultantes
en orden alfabético.
El archivo romeo.txt puede descargarse desde el
Campus Virtual
'''

# Variables
nomFichero=''
fichero = None


def leerLineas(fichero):
	palabrasLineas = []
	palabrasLineasSort = []
	for linea in fichero:
		for palabra in linea.split():	
			
			if palabra not in palabrasLineas :				
				palabrasLineas.append(palabra)
									
	palabrasLineas.sort()
	print('- Lista sort(): ')
	print(palabrasLineas)		
	ordenarPalabras(palabrasLineas)
	
def ordenarPalabras(palabrasLineas):
	alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	palabrasListatMP = []	

	for letra in alfabeto:
		for palabra in palabrasLineas:			
			if palabra[0].upper() == letra.upper():
				palabrasListatMP.append(palabra)
	
	

	print('- Prueba orden minimo alfabetica:')
	for palabra in palabrasListatMP:				
		print(palabra)
			
			
# Main
nomFichero = input('Introduzca nombre del fichero: ')

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
