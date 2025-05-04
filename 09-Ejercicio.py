# Autor: Francisco J. Becerra
# Fecha: 04/05/2025
# Curso: UMA - Python para principiantes
# Tema: 4
# Ejercicio: 09-Ejercicio.py

# Condición previa:
'''
Requiere el fichero
- mbox-short.txt
'''

# Descripción:
'''
Escribe un programa que lea el archivo mbox-
short.txt e indique quién ha enviado el mayor
número de e-mails junto con el número de e-
mails. El programa busca líneas con ‘From ‘ y
toma la segunda palabra de estas líneas como la
persona que envió el e-mail.
Debes crear un diccionario Python que mapea el
nombre del emisor con el número de veces que
aparece en el archivo. Después de generar el
diccionario, el programa itera a través del
diccionario para ver quién ha sido el emisor con
más mensajes.
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
				
	calcularRemitentes(direcciones)	
	
	print('-----------------')		
	print('Direcciones email incluidas: '+str(incluidos))
	print('Direcciones email excluidos: '+str(excluidos))
	
def calcularRemitentes(direcciones):
	diccionarioRemitentes = {}	
	remitenteMayorNumeroEmails = []
	
	# Incluir direcciones	
	for direccion in direcciones:		
		if direccion[1] not in diccionarioRemitentes:
			diccionarioRemitentes[direccion[1]] = 1
		else:
			diccionarioRemitentes[direccion[1]] = diccionarioRemitentes[direccion[1]] + 1
	
	# Localizar quien envio el mayor numero de mensajes	
	primerElemento = True
	for key,valor in diccionarioRemitentes.items() :
		print('Emails enviados por: '+key+' ['+str(valor)+']')
		
		if primerElemento == True:
			remitenteMayorNumeroEmails.append(key)
			remitenteMayorNumeroEmails.append(valor)
			primerElemento = False 
		else:
			if valor > remitenteMayorNumeroEmails[1]:
				remitenteMayorNumeroEmails[0] = key
				remitenteMayorNumeroEmails[1] = valor

	print('......................')
	print('Mayor emisor mensajes: '+remitenteMayorNumeroEmails[0]+' ['+str(remitenteMayorNumeroEmails[1])+']')			
	
			
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
