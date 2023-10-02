# 1) Crear un programa que contenga las funciones:
#   a - generarDatos(n) que devuelve una lista de n numeros enteros aleatorios
#     entre 0 y 100
#   b - guardarDatos(nombre, datos) que guarda los elementos de una lista en un archivo 
#     (uno por renglon)

import random
def generarDatos(n):
    l = []
    i = 0
    while(i < n):
        l.append(random.randint(0, 100))
        i+=1
    return l

def guardarDatos(nombre, datos):
    file = open(nombre, "w")
    for x in datos:
        file.write(str(x)+"\n")

r = generarDatos(10)
guardarDatos("Clases/archivo1.txt", r)


# 2) Crear un programa que contenga las funciones
#   a - leerDatos(nombre) que lee los datos contenidos en un archivo
#   b - convertirDatos(entrada) que transforma los datos leidos del archivo en una lista 
#       de enteros
#   c - convertirDatosLambda(entrada) que transforma los datos leidos del archivo en una lista
#       de enteros mediante listas por comprension
#   d - noRepetidos(daots) que devuelve una lista de los elemenos no repetidos (no usar for - in)

def leerDatos(nombre):
    file = open(nombre, "r")
    return file.readlines()

def convertirDatos(entrada):
    ints = []
    for string in entrada:
        ints.append(int(string))
    return ints

def convertirDatosLambda(entrada):
    return [int(string) for string in entrada]

def noRepetidos(datos):
    return set(datos)

lista = leerDatos("Clases/archivo1.txt")
print("Datos sacados del archivo en formato lista con readLines")
print(lista)
lista_int = convertirDatos(lista)
print("Datos convertidos a int")
print(lista_int)
llista_int = convertirDatosLambda(lista)
print("Datos convertidos a int pero con lambdas")
print(llista_int)
set_int = noRepetidos(lista_int)
print("Datos convertidos a int sin repetir")
print(set_int)

# 3) crear un programa que contenga las funciones
#   a - leerDocumento(nombre) que lee los datos contenidos en un archivo de texto 
# conformados por palabras
#   b - palabrasLongitud(texto) que devuelve un mapa de las palabras distintas y la 
# cantidad de letras que tiene
#   c -  contarPalabras(texto) que devuelve el numero de palabras
#   d -  contarPalabrasDistintas(texto) que devuelve el numero de palabras distintas
#   e -  promedioLetras(palabras) que devuelve la cantidad promedio de letras entre 
# todas las palabras

def leerDocumento(nombre):
    file = open(nombre, "r")
    return file.readlines()

def palabrasLongitud(texto):
    d = dict()
    for x in texto:
        x = x.strip()
        stlist = x.split()
        for y in stlist:
            d[y] = len(y)
    return d

def contarPalabras(texto):
    l = []
    for x in texto:
        l = l + x.split()
    return len(l)

def contarPalabrasDistintas(texto):
    l = []
    for x in texto:
        l = l + x.split()
    s = set(l)
    return len(s)

lines = leerDocumento("Clases/archivo2.txt")
diccionario = palabrasLongitud(lines)
print("Mapa de palabras y su longitud")
print(diccionario)
print("Cantidad de palabras en el archivo")
print(contarPalabras(lines))
print("Cantidad de palabras en el archivo SIN repetir")
print(contarPalabrasDistintas(lines))