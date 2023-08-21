'''
Ejercicio 02
Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”
'''

from os import system
system('cls')

bandera = True

while bandera: 
    numero_regla = int(input("Ingrese un numero y le diremos la regla de estilo correspondiente del PEP "))
    while numero_regla < 1 or numero_regla > 8:
        numero_regla = int(input("Ingrese un numero valido "))

    if numero_regla == 1: 
        print("regla numero 1")
    elif numero_regla == 2: 
        print("regla numero 2")
    elif numero_regla == 3: 
        print("regla numero 3")
    elif numero_regla == 4: 
        print("regla numero 4")
    elif numero_regla == 5: 
        print("regla numero 5")
    elif numero_regla == 6: 
        print("regla numero 6")
    elif numero_regla == 7: 
        print("regla numero 7")
    elif numero_regla == 8: 
        print("regla numero 8")

    continuar = input("Desea continuar?").lower()
    if continuar == "no":
        bandera = False
