## Ejercicio 6 Juan David Saavedra Jaimez C.C 1095798802

def fibonacci(n_terms):
    # Generar la secuencia de Fibonacci hasta n términos
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n_terms):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_pares(n_terms):
    # Generar los números Fibonacci pares hasta n términos
    fib_sequence = fibonacci(n_terms)
    fib_pares = [num for num in fib_sequence if num % 2 == 0]
    return fib_pares

def suma_fibonacci_en_rango(start, end):
    # Generar la secuencia de Fibonacci y sumar los números dentro del rango [start, end]
    a, b = 0, 1
    suma = 0
    while a <= end:
        if a >= start:
            suma += a
        a, b = b, a + b
    return suma

# Ejemplo de uso
n_terms = int(input("Ingrese el número de términos de la secuencia de Fibonacci: "))
resultado_fibonacci = fibonacci(n_terms)
resultado_fibonacci_pares = fibonacci_pares(n_terms)

print(f"Secuencia de Fibonacci hasta {n_terms} términos: {resultado_fibonacci}")
print(f"Números Fibonacci pares: {resultado_fibonacci_pares}")

# Rango de suma de Fibonacci
start = int(input("Ingrese el valor de inicio del rango: "))
end = int(input("Ingrese el valor final del rango: "))
suma_en_rango = suma_fibonacci_en_rango(start, end)

print(f"La suma de los números Fibonacci en el rango [{start}, {end}] es: {suma_en_rango}")
