#D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)

def calcular_maximo(lista:list)->int:
    flag_primero = True
    for tema in lista:
        if flag_primero == True or tema['views'] > maxima_views:
            maxima_views = tema["views"]
            flag_primero = False
    return maxima_views


def mostrar_maximo(lista:list, maxima_views:int)->None:
    for tema in lista:
        if tema['views'] == maxima_views:
            print(f"{tema['title']}")



def buscar_temas_mas_views(lista:list):
    #me guardo el retorno de la funcion "calcular maximo"--> solo calcula el numero maximo de reproducciones
    maxima_views = calcular_maximo(lista) #llamada a la funcion: (con parametro lista que es el mismo del principal)

    #ese valor lo utilizo para mostrar la cantidad 
    print(f"cantidad maxima de reproduccion: {maxima_views}")

    #uso esta funcion para imprimir a que artista/s corresponde esa cantidad maxima de views 
    mostrar_maximo(lista, maxima_views) #llamada a la funcion:parametro mismo del principal y maxima_views (del retorno de la funcion calcular_maximo)