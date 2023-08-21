####FUNCIONES AVANZADAS############


from os import system
system('cls')
from data import lista_bzrp



def mostrar_lista_temas_views():
#C. Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
    for tema in lista_bzrp:
        print(f"{tema['title']} - {tema['views']}")


def calcular_maximo(lista:list, clave:str)->int:
    flag_primero = True
    #validar los tipos de datos que recibimos por parametro
    if(type(lista) == list and len(lista)>0 and type(clave) == str and len(clave)>0):
        #calcular el numero maximo de la clave pasada por parametro(pyede ser duracion, cantidad de reproducciones etc)
        for tema in lista:
            if flag_primero == True or tema[clave] > maximo:
                maximo = tema[clave]
                flag_primero = False
    return maximo


def mostrar_lista_temas(lista:list, clave=None,valor=None):
    if clave is None and valor is None:
        for tema in lista:
            print(f"{tema['title']}")
    else:
        #algoritmo de encontrar que claves coinciden con la maxima duracion o vistas o lo que sea (tmb para verificar si hay mas de uno)
        for tema in lista:
            if tema[clave] == valor:
                print(f"{tema['title']}")


#CON RESPECTO A CLAVE VIEWS
def buscar_temas_mas_views(lista:list):
    #me guardo el retorno de la funcion "calcular maximo"--> solo calcula el numero maximo de la clave pasada por parametro->en este caso 'views'
    maxima_views = calcular_maximo(lista, "views") #llamada a la funcion: (con parametro lista que es el mismo del principal)

    #ese valor lo utilizo para mostrar la cantidad 
    print(f"cantidad maxima de reproduccion: {maxima_views}")

    #uso esta funcion para imprimir a que artista/s corresponde esa cantidad maxima de views 
    mostrar_lista_temas(lista, 'views',maxima_views) #llamada a la funcion:parametro mismo del principal y maxima_views (del retorno de la funcion calcular_maximo)

#CON RESPECTO A CLAVE DURACION
def buscar_temas_mas_largos(lista:list):
    maximo_len = calcular_maximo(lista, 'length')
    print(f"Duracion maxima {maximo_len}")
    mostrar_lista_temas(lista, 'length', maximo_len)



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
            mostrar_lista_temas(lista_bzrp) #como no pase mas parametros, quedan por default en none (entra al if)
        case 2:
            buscar_temas_mas_largos(lista_bzrp)#llamada a la funcion, esta tiene dentro 'mostrar_lista_temas' que ahi si utiliza los parametros opcionales,
                                                #entra al else
            #mostrar_lista_temas_views()
        case 3:
            buscar_temas_mas_views(lista_bzrp)
        case 4:
            buscar_temas_menos_views()
        case 5:
            calcular_promedio()
        case 6:
            break




