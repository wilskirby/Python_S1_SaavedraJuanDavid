import math
## Se necesita math para hacer sus procesos de permutación

## El valueError es para cuando algo no va segun lo previsto fallar y dar un mensaje de pq no funciona 

def factorial(n):
    ## Uso de factorial para n math.factorial(n)
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    return math.factorial(n)

def combinaciones(n, b):
    ## Uso de las combinatorias segun n,b math.comb(n, b)
    if n < 0 or b < 0:
        raise ValueError("Los valores de n y b deben ser no negativos.")
    if b > n:
        raise ValueError("b no puede ser mayor que n.")
    return math.comb(n, b)

def permutaciones(n, b):
    ## Uso de la permutacion math.perm(n, b)
    if n < 0 or b < 0:
        raise ValueError("Los valores de n y b deben ser no negativos.")
    if b > n:
        raise ValueError("b no puede ser mayor que n.")
    return math.perm(n, b)

# Menu de escribir

n = int(input("Ingrese el valor de n: "))
b = int(input("Ingrese el valor de b para las combinaciones y permutaciones: "))

print(f"Factorial de {n}: {factorial(n)}")
print(f"Combinaciones de {n} sobre {b} (nCr): {combinaciones(n, b)}")
print(f"Permutaciones de {n} sobre {b} (nPr): {permutaciones(n, b)}")

