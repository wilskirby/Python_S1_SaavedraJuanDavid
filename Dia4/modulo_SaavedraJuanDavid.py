def ejecutar_programa():

    nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
    ]
    
    apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
    ]
    
    while True:
        print("\nBienvenido al programa de lista de estudiantes")
        print("1. Agregar estudiante")
        print("2. Ver estudiantes")
        print("3. Editar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opc = input(": ")
        
        if opc == "1":
            agregar_estudiante(nombres, apellidos)
        elif opc == "2":
            ver_estudiantes(nombres, apellidos)
        elif opc == "3":
            editar_estudiante(nombres, apellidos)
        elif opc == "4":
            eliminar_estudiante(nombres, apellidos)
        elif opc == "5":
            break
        else:
            print("Opción inválida.")

def agregar_estudiante(nombres, apellidos):
    n1 = input("Ingrese el primer nombre del estudiante: ")
    n2 = input("Ingrese el segundo nombre (si lo tiene): ")
    ap1 = input("Ingrese el primer apellido: ")
    ap2 = input("Ingrese el segundo apellido: ")
    nombres.append([n1, n2])
    apellidos.append([ap1, ap2])

def ver_estudiantes(nombres, apellidos):
    for i, (nombre, apellido) in enumerate(zip(nombres, apellidos), 1):
        print(f"Estudiante #{i}: {' '.join(nombre)} {' '.join(apellido)}")

def editar_estudiante(nombres, apellidos):
    ver_estudiantes(nombres, apellidos)
    edt = int(input("Ingrese el número del estudiante a editar: ")) - 1
    
    if 0 <= edt < len(nombres):
        if len(nombres[edt]) == 2:
            o = int(input("1. Primer nombre\n2. Segundo nombre\n: "))
            nombres[edt][o - 1] = input("Ingrese el nombre corregido: ")
        else:
            nombres[edt][0] = input("Ingrese el nombre corregido: ")
        
        if len(apellidos[edt]) == 2:
            t = int(input("1. Primer apellido\n2. Segundo apellido\n: "))
            apellidos[edt][t - 1] = input("Ingrese el apellido corregido: ")
        else:
            apellidos[edt][0] = input("Ingrese el apellido corregido: ")
    else:
        print("Número inválido.")

def eliminar_estudiante(nombres, apellidos):
    ver_estudiantes(nombres, apellidos)
    el = int(input("Ingrese el número del estudiante a eliminar: ")) - 1
    if 0 <= el < len(nombres):
        nombres.pop(el)
        apellidos.pop(el)
    else:
        print("Número inválido.")

if __name__ == "__main__":
    ejecutar_programa()
