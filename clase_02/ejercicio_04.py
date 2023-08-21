'''
La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.

Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).

Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.

Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
---------------------------------------------------------------------
'''


from os import system
system('cls')

acumulador_peso = 0
acumulador_precio_bruto = 0
bandera_tipo_mas_caro = True

for compra in range(2):
    #1. PESO: (entre 10 y 100 kilos)
    peso = int(input('ingrese peso'))
    while peso < 10 or peso > 100:
        peso = int(input('ingrese peso, debe ser entre 10 y 100 kilos'))

    precio_por_kilo = int(input("ingrese el precio por kilo"))
    while precio_por_kilo < 0:
        precio_por_kilo = int(input("ingrese el precio por kilo, debe ser mayor a 0"))
    
    tipo_variedad = input("Ingrese variedad}: vegetal, animal o mezcla")
    while tipo_variedad != "vegetal" and tipo_variedad != "mezcla" and tipo_variedad != "animal":
        tipo_variedad = input("Ingrese variedad: vegetal, animal o mezcla")
    
    if bandera_tipo_mas_caro:
        precio_mas_caro = precio_por_kilo
        tipo_mas_caro = tipo_variedad
        bandera_tipo_mas_caro = False
    else:
        if precio_por_kilo > precio_mas_caro:
            precio_mas_caro = precio_por_kilo
            tipo_mas_caro = tipo_variedad


    acumulador_precio_bruto += precio_por_kilo*peso 
    acumulador_peso += peso


if acumulador_peso > 300:
    precio_con_descuento = acumulador_precio_bruto * 0.75
else:
    if acumulador_peso > 100:
        precio_con_descuento = acumulador_precio_bruto * 0.85
    else:
        precio_con_descuento = acumulador_precio_bruto

promedio_precio_por_kilo = acumulador_precio_bruto/acumulador_peso

print(f"El importe total a pagar bruto (sin descuento) es de ${acumulador_precio_bruto} ")
print(f"El importe total a pagar con descuento es ${precio_con_descuento}")
print(f"El tipo mas caro es {tipo_mas_caro}")
print(f"El promedio de precio por kilo en total es: ${promedio_precio_por_kilo}")