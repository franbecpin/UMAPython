# Autor: Francisco J. Becerra
# Fecha: 04/05/2025
# Curso: UMA - Python para principiantes
# Tema: 4
# Ejercicio: 08-Ejercicio-2.py

# Condición previa:
'''
Requiere el fichero
- mbox-short.txt
'''

# Descripción:
'''
Abre el archivo mbox-short.txt y léelo línea a línea. Cuando
encuentres una línea que comience con 'From ' como la
siguiente:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16
2008
trocea la línea usando split() e imprime la segunda palabra
de la línea (es decir, la dirección de la persona que envió el
mensaje). Al final, indica cuántas personas hubo (no es
necesario tener en cuenta repeticiones).
Nota: asegúrate de no incluir las líneas que comiencen con
'From:'.
El archivo mbox-short.txt puede descargarse desde el
Campus Virtual
'''

# Variables
nomFichero=''
fichero = None
valorBusqueda = 'From'
valorExclusion = 'From:'

def leerLineas(fichero):
	direcciones = []
	incluidos = 0
	excluidos = 0
	
	for linea in fichero:
		if linea.startswith(valorBusqueda) :
			if linea.split()[0] != valorExclusion:
				incluidos = incluidos + 1
				direcciones.append(linea.split())
			else:
				excluidos = excluidos +1	
	
	print('Direcciones email:')
	print('------------------')
	index = 1
	for direccion in direcciones:
		print('['+str(index)+']'+direccion[1])	
		index = index + 1	

	print('-----------------')	
	print('Direcciones email incluidas: '+str(incluidos))
	print('Direcciones email excluidos: '+str(excluidos))
			
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
