########INTRODUCCION A FUNCIONES#########


from os import system
system('cls')
from clase_06.data import lista_bzrp

def mostrar_lista_temas():
#B. Recorrer la lista imprimiendo por consola el título de cada video
    for tema in lista_bzrp:
        print(f"{tema['title']}")

def mostrar_lista_temas_views():
# #C. Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
    for tema in lista_bzrp:
        print(f"{tema['title']} - {tema['views']}")

def buscar_temas_mas_views():
    #D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)
    flag_primero = True
    for tema in lista_bzrp:
        if flag_primero == True or tema['views'] > maxima_views:
            maxima_views = tema["views"]
            flag_primero = False

    print(f"cantidad maxima de reproduccion: {maxima_views}")

    for tema in lista_bzrp:
        if tema['views'] == maxima_views:
            print(f"{tema['title']}")

def buscar_temas_menos_views():
#E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones(MÍNIMO)
    flag_primero = True
    for tema in lista_bzrp:
        if flag_primero == True or tema['views'] < minima_views:
            minima_views = tema["views"]
            flag_primero = False

    print(f"cantidad minima de reproduccion: {minima_views}")

    for tema in lista_bzrp:
        if tema['views'] == minima_views:
            print(f"{tema['title']}")


def calcular_promedio():
    #F. Recorrer la lista y determinar la cantidad total de reproducciones del canal (ACUMULADOR)
    acumulador_views = 0
    for tema in lista_bzrp:
        acumulador_views += tema['views']

    print(f"Sumatoria de reproducciones: {acumulador_views}")

    #G. Recorrer la lista y determinar la cantidad promedio de reproducciones que tiene un video (PROMEDIO)
    contar_temas = 0
    for tema in lista_bzrp:
        contar_temas += 1
    promedio_views = acumulador_views/ contar_temas
    print(f"El promedio de visitas es {promedio_views}")



menu = ["1.Mostrar temas", "2.Mostrar temas con vistas","3.Mostrar temas con mas vistas","4.Mostrar temas con menos vistas","5.Mostrar promedio reproduciones","6.Salir","Elija una opcion"]

def mostrar_menu():
    for opcion in menu:
        print(opcion)


while True:
    mostrar_menu()
    respuesta = int(input("Ingrese una opcion: "))
    match respuesta:
        case 1:
            mostrar_lista_temas()
        case 2:
            mostrar_lista_temas_views()
        case 3:
            buscar_temas_mas_views()
        case 4:
            buscar_temas_menos_views()
        case 5:
            calcular_promedio()
        case 6:
            break


#B. Recorrer la lista imprimiendo por consola el título de cada video
#lo mismo con range
# for i in range(len(lista_bzrp)):
#     print(f"{lista_bzrp[i]['title']}")


