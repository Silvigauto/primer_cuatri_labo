from os import system
system('cls')

#WHILE
#----primera forma---
# acumulador = 0
# seguir = "si"

# while seguir == "si":
#     numero = int(input("Ingrese un numero:"))
#     acumulador += numero

#     seguir = input("desea continuar?")

# print(f"Acumulado: {acumulador}")

#----otra forma cambiando la condicion-----
# acumulador = 0
# seguir = True

# while seguir:
#     numero = int(input("Ingrese un numero:"))
#     acumulador += numero

#     seguir = input("desea continuar?")
#     if seguir == "si":
#         seguir = True
#     else:
#         seguir = False

# print(f"Acumulado: {acumulador}")

#----una forma de simular un do while con break -----

# acumulador = 0


# while True:
#     numero = int(input("Ingrese un numero:"))
#     acumulador += numero

#     seguir = input("desea continuar?")
#     if seguir != "si":
#         break

# print(f"Acumulado: {acumulador}")

#FOR --> cuando sabemos la cantidad de veces que va a iterar
#range

#imprime la lista desde el 0 hasta el ult numero menos uno
# lista_numeros = list(range(5))
# print(lista_numeros) #[0, 1, 2, 3, 4]

#ejemplo con range
# acumulador = 0
# #se realizan 5 iterciones
# for x in range(5):
#     numero = int(input("ingrese un numero: "))
#     acumulador += numero
# print(f"Acumulado: {acumulador}")

#ejemplo for (inmutable)
# lista_nombres = ["Luis", "Nicolas", "Federico", "Micaela", "Silvina"]
# for nombre in lista_nombres:
#     print(nombre)

#break
# lista_numeros = [1,2,4,6,7]
# for numero in lista_numeros:
#     if(numero==4):
#         break #rompe y sale del bucle
#     print(numero, end=" ") #1 2

#continue
# lista_numeros = [1,2,4,6,7]
# for numero in lista_numeros:
#     if(numero==4):
#         continue #se lo saltea y sigue
#     print(numero, end=" ") #1 2 6 7

#match
color = input("ingrese un color").lower()
match color:
    case"azul":
        print("es azul")
    case"rojo":
        print("es rojo")
    case"amarillo":
        print("es amarillo")
    case"verde":
        print("es verde")
    case _: #DEFAULT DEL MATCH EN PYTHON (OTHER)
        print("otro color")