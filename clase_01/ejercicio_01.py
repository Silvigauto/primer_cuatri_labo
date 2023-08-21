'''
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo (barbijo, jabón o alcohol)
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.
'''
from os import system
system('cls')

tipo = input("Ingrese el tipo: Barbijo / Jabon / Alcohol").lower()
while (tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
    tipo = input("Error : Ingrese el tipo: Barbijo / Jabon / Alcohol")

precio = int(input('Ingrese el precio'))
while precio < 0:
    precio = int(input('Ingrese el precio'))

cantidad_unidades = int(input('Ingrese la cantidad de unidades'))  
while cantidad_unidades < 0:
    cantidad_unidades = int(input('Ingrese la cantidad de unidades')) 

marca = input('Ingrese la marca')

fabricante = input('Ingrese el fabricante')

print(f"Tipo:{tipo}\nPrecio:{precio}\nCantidad de unidades:{cantidad_unidades}\nMarca:{marca}\nFabricante:{fabricante}")