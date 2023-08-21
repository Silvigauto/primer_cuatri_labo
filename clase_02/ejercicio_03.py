'''
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.

No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:

A. El promedio de edad de las votantes de género femenino 
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)
'''
from os import system
system('cls')

respuesta = "si"
acumulador_edad_femenino = 0
contador_edad_femenino = 0
contador_masculino_2540 = 0
contador_votos_julieta = 0
contador_votos_marcos = 0
contador_votos_nacho = 0
contador_votos_total = 0
bandera_votante_mas_joven_nacho = True


while respuesta == "si":
    nombre = input("ingrese su nombre")
    while nombre == "":
        nombre = input("ingrese su nombre")

    edad = int(input("ingrese su edad"))
    while edad < 13:
        edad = int(input("ingrese su edad, debe ser mayor de 13 para votar"))

    genero = input("ingrese su genero: Femenino/Masculino/Otro")
    while genero != "femenino" and genero != "masculino" and genero != "otro":
        genero = input("ingrese su genero: Femenino/Masculino/Otro")
    
    voto = input("A quien va a votar? Julieta, Marcos o Nacho")
    while voto != "julieta" and voto != "marcos" and voto != "nacho":
        voto = input("A quien va a votar? Julieta, Marcos o Nacho")

    #A. El promedio de edad de las votantes de género femenino
    if genero == "femenino":
        acumulador_edad_femenino += edad
        contador_edad_femenino += 1
    
    #B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.
    if genero == "masculino" and (edad > 24 and edad < 41) and (voto == "nacho" or voto == "julieta"):
        contador_masculino_2540 += 1
    
    #D. Nombre de cada participante y porcentaje de los votos qué recibió. match y contador votos cada uno + contador votos general
    match voto:
        case "julieta":
            contador_votos_julieta += 1
        case "marcos":
            contador_votos_marcos += 1
        case "nacho":
            contador_votos_nacho += 1
            if bandera_votante_mas_joven_nacho:
                edad_votante_mas_joven_nacho = edad
                nombre_votante_mas_joven_nacho = nombre
                bandera_votante_mas_joven_nacho = False
            else:
                if edad < edad_votante_mas_joven_nacho:
                    edad_votante_mas_joven_nacho = edad
                    nombre_votante_mas_joven_nacho = nombre
    
    contador_votos_total += 1

    respuesta = input("desea continuar?").lower()
if contador_edad_femenino > 0:  
    promedio_edad_femenino = acumulador_edad_femenino/contador_edad_femenino
else:
    promedio_edad_femenino = "No hay promedio que calcular"

if contador_votos_nacho == 0:
    nombre_votante_mas_joven_nacho = 'No hubo votos para Nacho'

porcentaje_julieta = (contador_votos_julieta/contador_votos_total) * 100
porcentaje_marcos = (contador_votos_marcos/contador_votos_total) *100
porcentaje_nacho = (contador_votos_nacho/contador_votos_total)*100


#E. El nombre del participante que ganó el reality (El que tiene más votos)

if contador_votos_nacho > contador_votos_marcos and contador_votos_nacho > contador_votos_julieta:
    ganador = "Nacho"
else:
    if contador_votos_julieta > contador_votos_marcos:
        ganador = "Julieta"
    else:
        ganador = "Marcos"


print(f"Promedio de edad de las votantes de genero femenino: {promedio_edad_femenino}")
print(f"Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta. {contador_masculino_2540}")
print(f"Nombre del votante mas joven que voto a nacho: {nombre_votante_mas_joven_nacho}")
print(f"-PORCENTAJES DE VOTOS-\nJulieta:{porcentaje_julieta}\nMarcos:{porcentaje_marcos}\nNacho:{porcentaje_nacho}")
print(f"El ganador/a es {ganador}")