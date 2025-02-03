##Ejercicio 1 Juan David Saavedra Jaimez C.C 1095798802

##Convertir proceso

def convertir_a_celsius(f):
    c = (5/9) * (f - 32)
    return c

# Funcion de C a F
def convertir_a_fahrenheit(c):
    f = (9/5) * c + 32
    return f


opcion= (input("Ingresa F para convertir de fahrenheit a celsius y ingresa C para convertir de Celsius a fahrenheit: ")).upper()

if opcion == "F":
    f = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    c = convertir_a_celsius(f)
    print (f"Los grados Fahrenheit {f} son a {c} grados Celsius.")
    
elif opcion == 'C':
    c = float(input("Ingrese la temperatura en grados Celsius: "))  
    f = convertir_a_fahrenheit(c)  
    print(f"{c} grados Celsius son {f} grados Fahrenheit.")