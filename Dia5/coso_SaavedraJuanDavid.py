import json

def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['afo']
    base = inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000
    if inmueble['garaje']:
        base += 15000
    if inmueble['zona'] == 'A':
        precio = base * (1 - antiguedad / 100)
    else:
        precio = base * (1 - antiguedad / 100) * 1.5
    return precio

def buscar_inmuebles_por_presupuesto(inmuebles, presupuesto):
    resultados = []
    for inmueble in inmuebles:
        precio = calcular_precio(inmueble)
        if precio <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio
            resultados.append(inmueble_con_precio)
    return resultados





def menu():
    inmuebles = {}
    while True:
        print(" Menú ")
        print("1. Buscar inmuebles por presupuesto")
        print("2. Agregar inmueble")
        print("3. Mostrar inmuebles")
        print("4. Actualizar inmueble")
        print("5. Eliminar inmueble")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")