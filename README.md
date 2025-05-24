# UMA - Python
## Repositorio para el curso UMA
## Python para principiantes
![Static Badge](https://img.shields.io/badge/En%20desarrollo%20-%20?label=Status&labelColor=orange)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/franbecpin/UMAPython/main)
![GitHub number of milestones](https://img.shields.io/github/milestones/open/franbecpin/UMAPython)  
![GitHub Tag](https://img.shields.io/github/v/tag/franbecpin/UMAPython)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/franbecpin/UMAPython)
![GitHub repo file or directory count](https://img.shields.io/github/directory-file-count/franbecpin/UMAPython)


---
## Descripción
Repositorio asociado al curso:
- Entidad: Universidad de Málaga
- Curso: Python para principiantes
- Descripción: Curso para el aprendizaje de Python   
- Tecnología / Versión:
	- ![Static Badge](https://img.shields.io/badge/Python%20-%203.6.9-green)
	

## Índice
---
- [Tema 1](#Tema-1)
- [Tema 2](#Tema-2)
- [Tema 3](#Tema-3)
- [Tema 4](#Tema-4)

---
## Tema 1
### Descripción
- Python-01-IntroducciónArchivo
- Python-01-IntroArchivo
- Python-01-Intro-2 Arquitectura HardwareArchivo
- Python-01-Intro-3 Hablando con PythonArchivo
- Python-02-Variables Expresiones SentenciasArchivo
- Python-02-01-VariablesArchivo
- Python-02-02-ExpresionesArchivo
- Python-02-03-TiposArchivo
- **02-Ejercicio** [X]

### 02-Ejercicio
```
Escribir un programa que pregunte al usuario un número 
de horas y el precio por hora para calcular el total a pagar.  
    
    Introduzca las horas: 35  
    Introduzca el precio/hora: 2.75  
    Total: 96.25  
```
#### Ficheros:
	- 02-Ejercicio.py

#### Ejecución
```python
python3 02-Ejercicio.py
```

---
## Tema 2
### Descripcion
- Python-03-Ejecución condicionalArchivo
- Python-03-01-Sentencias condicionalesArchivo
	- **03-Ejercicio-1** [X]
 	- **03-Ejercicio-2** [X]
- Python-03-02-Decisiones anidadasArchivo
- Python-03-03-Estructura try exceptArchivo
- Python-04-FuncionesArchivo
- 	- **04-Ejercicio** [X]
- Python-04-Funciones lambda (material no incluido en los vídeos)Archivo
	- Python-04-01-FuncionesArchivo
	- Python-04-02-Funciones propiasArchivo
- Python-05-BuclesArchivo
	- Python-05-01-BuclesArchivo
	- Python-05-02-Bucles definidosArchivo
	- Python-05-03-Bucles Encontrar el maximoArchivo
	- Python-05-04-Bucles EjemplosArchivo
 	- **05-Ejercicio** [X]


### 03-Ejercicio-1
```
Reescribe el programa de pagos para incrementar en un
factor de 1.5 las horas que se trabajen por encima de 40
horas (hasta 40 horas todas se cobran a precio normal)
	Introduzca las horas: 45
	Introduzca el precio/hora: 10
	Total: 475.0 475 = 40 * 10 + 5 * 15
```

### 03-01-Ejercicio 2
```
Reescribe el programa de pagos usando try y except para
que se manejen adecuadamente entradas no numéricas
(nota: no hace falta quese vuelvan a pedir los números si falla)
	Introduzca las horas: 20
	Introduzca el precio/hora: nueve
	Error, por favor introduzca un número
	Introduzca las horas: cuarenta
	Error, por favor introduzca un número
```
#### Ficheros:
- 03-Ejercicio-1.py
- 03-Ejercicio-2.py

#### Ejecución
```python
python3 03-Ejercicio-1.py
python3 03-Ejercicio-2.py
```

### 04-Ejercicio
```
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
```
#### Ficheros:
- 04-Ejercicio.py

#### Ejecución
```python
python3 04-Ejercicio.py
```
### 05-Ejercicio
```
Escribe un programa que pida números al usuario hasta
que escriba 'fin'. Una vez escrito 'fin', el programa debe
mostrar el número más grande y el más pequeño. Si el
usuario escribe algo diferente a un número, se debe
capturar con un try/except e ignorar el valor introducido.
Probar con 7, 2, bob, 10, y 4
Nota: el ejercicio debe resolverse con los visto hasta el
momento. No está permitido el uso de otros elementos
como listas (que se verán posteriormente)
```
#### Ficheros:
- 05-Ejercicio.py

#### Ejecución
```python
python3 05-Ejercicio.py
```
## Tema 3
### Descripcion

- Python-06-StringsArchivo
	- **06-Ejercicio-1 [X]**
 	- **06-Ejercicio-2 [X]**
  	- **06-Ejercicio-3 [X]**
- Python-06-Strings (contenido adicional) (material no incluido en los vídeos)Archivo
- Python-06-01-StringsArchivo
- Python-06-02-Operaciones con StringsArchivo
- Python-06-03-Funciones para StringsArchivo
- Python-07-Archivos
	- **07-Ejercicio [X]**
- Python-07-01-Archivos
- Python-07-02-Procesando Archivos

### 06-Ejercicio-1
```
Utilizar find() y los slices (:) para extraer el número en un
string como el que aparece a continuación. Convertir el
número a flotante y mostrarlo.
¡Ojo! No asumir que el número es 0.8475, es solo un
ejemplo. No sabemos qué número es, tenemos que
extraerlo. Sí podemos suponer que el resto de la línea es
igual. Esto es, comienza por "X-DSPAM-Confidence..."
"X-DSPAM-Confidence: 0.8475"
```

### 06-Ejercicio-2
```
Pedir un nombre al Usuario de la forma:
NOMBRE APELLIDO1 APELLIDO2
Por ejemplo: José García Pérez
Dar la Vuelta al nombre y presentarlo en el formato:
APELLIDO1 APELLIDO2, NOMBRE
Por ejemplo: García Pérez, José
```

### 06-Ejercicio-3
```
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
```

### 07-Ejercicio
#### Requiere los ficheros
- mbox-short.txt
- mbox.txtmbox.txt

```
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
```

#### Ficheros:
- 06-Ejercicio-1.py
- 06-Ejercicio-2.py
- 06-Ejercicio-3.py
- 07-Ejercicio.py

#### Ejecución
```python
python3 06-Ejercicio-1.py
python3 06-Ejercicio-2.py
python3 06-Ejercicio-3.py
python3 07-Ejercicio.py
```

---
## Tema 4
### Descripción

- Python-08-Listas en PythonArchivo  
	- **08-Ejercicio-1 [X]**  
	- **08-Ejercicio-2 [X]**  
- Python-08-01-ListasArchivo  
- Python-08-02-Metodos de ListasArchivo  
- Python-08-03-Listas y StringsArchivo  
- Python-09-Diccionarios en PythonArchivo  
	- **09-Ejercicio [X]**
- Python-09-01-DiccionariosArchivo  
- Python-09-02-Diccionarios Nombre mas comunArchivo  
- Python-09-03-Diccionarios Contando palabrasArchivo  
- Python-10-TuplasArchivo  
	- **10-Ejercicio [X]**
- Python-10-01-TuplasArchivo  
- Python-10-02-Mas sobre tuplasArchivo  

### 08-Ejercicio-1
#### Requiere los ficheros
- romeo.txt

```
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
```
### 08-Ejercicio-2
#### Requiere los ficheros
- mbox-short.txt

```
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
```

### 09-Ejercicio
#### Requiere los ficheros
- mbox-short.txt

```
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
```

### 10-Ejercicio
#### Requiere los ficheros
- mbox-short.txt

```
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
```

#### Ficheros:
- 08-Ejercicio-1.py
- 08-Ejercicio-2.py
- 09-Ejercicio.py
- 10-Ejercicio.py

#### Ejecución
```python
python3 08-Ejercicio-1.py
python3 08-Ejercicio-2.py
python3 09-Ejercicio-2.py
python3 10-Ejercicio.py
```
