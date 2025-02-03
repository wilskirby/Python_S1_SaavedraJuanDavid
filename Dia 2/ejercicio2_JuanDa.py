##Ejercicio 2 Juan David Saavedra Jaimez C.C 1095798802

##proceso inicial

def int_simple(prin,tasa, time):
    return (prin * tasa * time) / 100

def int_compuesto(prin, tasa, time, n):
    return prin * (1 + (tasa / (100 * n)))**(n * time) - prin

##Pedir datos al usuario

prin = float(input("Ingrese el monto principal: "))
tasa = float(input("Ingrese la tasa de interés anual : "))
time = float(input("Ingrese el tiempo en años: "))
n = int(input("Ingrese el número de veces que se compone el interés por año: "))

print("Interés simple:", int_simple(prin, tasa, time))
print("Interés compuesto:", int_compuesto(prin, tasa, time, n))