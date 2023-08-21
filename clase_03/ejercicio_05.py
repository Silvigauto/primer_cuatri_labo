'''
Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento de HR 
dispone de lista de justicieros pero solo tiene información detallada de algunos de ellos.
Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista 
heroes_info se puedan listar los datos de cada héroe con el siguiente formato:

'''

heroes_info = [
    {
        "Nombre":"Super Girl",
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    {
        "Nombre":"Shazam",
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson",
    },
    {
        "Nombre":"Power Girl",
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    {
        "Nombre":"Wonder Woman",
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
]

for heroe in heroes_info:
    print(f"\nID: {heroe['ID']}, Codename: {heroe['Nombre']}\nIdentidad: {heroe['Identidad']}, Origen {heroe['Origen']}")
    habilidades_seteadas = set(heroe['Habilidades'])
    print("Habilidades: ",end="")
    for habilidad in habilidades_seteadas:
        print(habilidad,end=" | ")
    print("\n------------------------------------")
    