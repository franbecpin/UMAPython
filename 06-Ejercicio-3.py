# Autor: Francisco J. Becerra
# Fecha: 03/05/2025
# Curso: UMA - Python para principiantes
# Tema: 3
# Ejercicio: 06-Ejercicio-3.py

# Condición previa:
'''
NINGUNA
'''

# Descripción:
'''
Pedir una contraseña al Usuario repetidas veces hasta que
la contraseña sea considerada fuerte. Para ello, debe tener,
como mínimo 8 caracteres y contener, al menos, tanto una
mayúscula como un dígito
estaEslaCon8traseña sería válida
abcdefghijklmnopq no sería válida porque no cumple las
condiciones
La solución debe incluir una función que reciba un string y
retorne si es una contraseña fuerte o no
Pista: usar las funciones isdigit, isupper
'''

# Variables
minimoCaracteres = 8
passwordAceptada = False
password =''

# ---
def comprobarMinimoCaracteres(password):
	cumpleMinimo = False
	if len(password) >= minimoCaracteres:
		cumpleMinimo = True
	
	return cumpleMinimo	

# ---
def comprobarContieneMayuscula(password):
	contieneMayuscula = False
	index = 0
	while index < len(password):
		if password[index].isupper() == True:
			contieneMayuscula = True
		
		index = index + 1
	
	return contieneMayuscula
	
# ---	
def comprobarContieneDigito(password):
	contieneDigito = False		
	index = 0
	while index < len(password):
		if password[index].isdigit() == True:
			contieneDigito = True
		
		index = index + 1
	
	return contieneDigito


while passwordAceptada == False and password.upper()!='FIN' :
	password=input('Introduzca la password [fin para cancelar]: ')	
	
	if password.upper()=='FIN' :
		break	
		
	if comprobarMinimoCaracteres(password) == False:
		print('[ERR] No contiene el minimo de caracteres ['+str(minimoCaracteres)+']')
		passwordAceptada = False
	else:
		if comprobarContieneDigito(password) == False:
			print('[ERR] La password debe contener al menos [1] numero')
			passwordAceptada = False
		else :
			if comprobarContieneMayuscula(password) == False:
				print('[ERR] La password debe contener al menos [1] Mayuscula')
				passwordAceptada = False
			else:
				passwordAceptada = True
	

if passwordAceptada == True :
	print('[OK] Password Aceptada')
else :
	print('Operacion Cancelada')
	
