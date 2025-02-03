import math

## Uso de directorios [] y {} directorio vacio

## if numero % 2 == 0: saber numero par o no
def clasificar_numero(numero):
    resultado = {}
    resultado["pares"] = "Par" if numero % 2 == 0 else "Impar"


##Numero primo range(2, int(math.sqrt(numero)) + 1), if numero % i == 0: saber si  es primo operacion

    if numero > 1:
        es_primo = True
        for i in range(2, int(math.sqrt(numero)) + 1):
            if numero % i == 0:
                es_primo = False
                break
        resultado["primo_o_no"] = "Primo" if es_primo else "Compuesto"
    else:
        resultado["primo_o_no"] = "No es primo ni compuesto"
    
    # Cuadrado perfecto para saber si es o no cuadrado perfecto math.isqrt(numero)
    raiz = math.isqrt(numero)
    resultado["cuadrado_perfecto"] = "Sí" if raiz * raiz == numero else "No"
    
    return resultado


numero = int(input("Ingrese un número: "))
resultado = clasificar_numero(numero)


print(f"El número {numero} es {resultado['pares']}, {resultado['primo_o_no']} y {'es' if resultado['cuadrado_perfecto'] == 'Sí' else 'no es'} un cuadrado perfecto.")
