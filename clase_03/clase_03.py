from os import system
system('cls')

'''
#LISTAS [] --> las listas son iterables


lista = [5,9,8,7,3,6,4]
print(lista)
print(f"Elemento 3:{lista[3]}")
#desde y hasta
print(lista[0:3]) #[1, 2, 3] (el 4 no lo agarra) el desde-> incluye hasta->excluye

l = range(10)
print(l) #range(0, 10)

acumulador = 0
#for (en base al indice)
for i in range(len(lista)):
    acumulador += lista[i]

#APPEND --> AGREGA UN DATO AL FINAL DE LA LISTA
print(acumulador)
lista.append(100)
print(lista)

#INSERT --> INSERTA UN DATO EN EL INDICE INDICADO (DATO, INDICE)
lista.insert(2,999)
print(lista)

#EXTEND --> AGREGA UN SUBLISTA(AL FINAL DE LA LISTA)
lista.extend([999,888,777])
print(lista)

#REMOVE -->remueve solo la primera ocurrencia. recibe el dato a eliminar
lista.remove(6)
print(lista)

#INDEX  --> DEVUELVE EL INDICE EN EL QUE SE ENCUENTRA EL DATO PASADO POR PARAMETRO
print(lista.index(999))

#for each (en base al dato)
for numero in lista:
    print(numero)
'''
'''
#DICCIONARIOS {} ITERABLE

#PRIMERA FORMA----------------
#LO CREO VACIO
mi_diccionario = {}

#LE ASIGNO UNA CLAVE-VALOR
mi_diccionario["Nombre"] = "Juan"

print(type(mi_diccionario)) #<class 'dict'>

#MOSTRAR TODOEL DICCIONARIO
print(mi_diccionario) #{'Nombre': 'Juan'}

#PARA ACCEDER A UN VALOR LO LLAMO POR LA CLAVE
print(mi_diccionario["Nombre"]) #Juan

mi_diccionario["Edad"] = 25
print(mi_diccionario["Edad"])

#SEGUNDA FORMA------------------
#LO CREO EN EL MOMENTO
otro_diccionario = {"Nombre": "Luis", "Edad": 32}

#LLAMO A LAS CLAVES
for key in otro_diccionario:
    print(key)  #Nombre Edad

#LLAMO A LOS VALORES
for key in otro_diccionario:
    print(otro_diccionario[key]) #Luis 32
'''

'''
#LISTAS PARALELAS
CANTIDAD_ALUMNOS = 3
lista_nombres = []
lista_apellidos = []

#USO RANGE PORQUE EN ESTE CASO ESTOY MODIFICANDO LA LISTA
for i in range(CANTIDAD_ALUMNOS):
    nombre = input("Ingrese nombre")
    apellido = input("Ingrese apellido")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

for i in range(CANTIDAD_ALUMNOS):
    print(f"{i+1})Nombre: {lista_nombres[i]} - Apellido {lista_apellidos[i]} ")
'''

'''
#LISTAS DE DICCIONARIOS
#lista_alumnos = []

lista_alumnos = [{'Nombre': 'juan', 'Apellido': 'perez', 'Edad': 25},
                {'Nombre': 'luis', 'Apellido': 'gomez', 'Edad': 64}, 
                {'Nombre': 'maria', 'Apellido': 'ruiz', 'Edad': 36}
                ]


# CANTIDAD_ALUMNOS = 3
# for i in range(CANTIDAD_ALUMNOS):
#     nombre = input("Ingrese nombre")
#     apellido = input("Ingrese apellido")
#     edad = int(input("Ingrese edad"))
#     un_alumno = {}
#     un_alumno["Nombre"] = nombre
#     un_alumno["Apellido"] = apellido
#     un_alumno["Edad"] = edad
#     lista_alumnos.append(un_alumno)

# print(lista_alumnos)

for alumno in lista_alumnos:
    edad = alumno["Edad"]
    if edad > 30:
        print(f"{alumno['Apellido']} - {alumno['Nombre']}- {edad}")
'''


#FOR ANIDADO
lista_alumnos_compleja = [
                        {'nombre': 'pepe', 'apellido':'argento', 'dni': '33', 'materias': ['matematica', 'literatura']},
                        {'nombre': 'moni', 'apellido':'ruiz', 'dni': '99', 'materias': ['ingles','matematica', 'biologia']},
                        {'nombre': 'coqui', 'apellido':'luz', 'dni': '77', 'materias': ['ingles']}
]

for alumno in lista_alumnos_compleja:
    nombre = alumno['nombre']
    apellido = alumno['apellido']
    dni = alumno['dni']
    materias = alumno['materias']
    print(f"-Ficha alumno-\nNombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nMaterias:")
    for materia in materias:
        print(materia)
    