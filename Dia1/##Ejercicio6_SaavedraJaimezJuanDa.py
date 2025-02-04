##Ejercicio 6 Juan David Saavedra Jaimez C.C 1095798802
hora = 20000

empleados = []
salarios_brutos = []
descuentos_eps = []
descuentos_pension = []
salarios_netos = []

n = int(input("Ingrese la cantidad de empleados: "))

for i in range(n):
    print(f"\nEmpleado {i + 1}:")
    nombre = input("Nombre del empleado: ")
    horas_trabajadas = float(input("Horas trabajadas: "))

    sueldo_bruto = horas_trabajadas * hora
    descuento_eps = sueldo_bruto * 0.04
    descuento_pension = sueldo_bruto * 0.04
    sueldo_neto = sueldo_bruto - descuento_eps - descuento_pension

    empleados.append((nombre, sueldo_neto))
    salarios_brutos.append(sueldo_bruto)
    descuentos_eps.append(descuento_eps)
    descuentos_pension.append(descuento_pension)
    salarios_netos.append(sueldo_neto)

    print(f"Sueldo bruto: ${sueldo_bruto:,.2f}")
    print(f"Descuento EPS: ${descuento_eps:,.2f}")
    print(f"Descuento Pensión: ${descuento_pension:,.2f}")
    print(f"Sueldo neto: ${sueldo_neto:,.2f}")

suma_salarios_brutos = sum(salarios_brutos)
suma_descuentos_eps = sum(descuentos_eps)
suma_descuentos_pension = sum(descuentos_pension)
suma_salarios_netos = sum(salarios_netos)
promedio_sueldo_bruto = suma_salarios_brutos / n
promedio_sueldo_neto = suma_salarios_netos / n

empleado_max = max(empleados, key=lambda x: x[1])
empleado_min = min(empleados, key=lambda x: x[1])


# Mostrar estadísticas finales
print("\nEstadisticas finales")
print(f"Total salarios brutos: ${suma_salarios_brutos:,.2f}")
print(f"Total descuentos EPS: ${suma_descuentos_eps:,.2f}")
print(f"Total descuentos Pensión: ${suma_descuentos_pension:,.2f}")
print(f"Total salarios netos: ${suma_salarios_netos:,.2f}")
print(f"Promedio sueldo bruto: ${promedio_sueldo_bruto:,.2f}")
print(f"Promedio sueldo neto: ${promedio_sueldo_neto:,.2f}")
print(f"Empleado que más gana: {empleado_max[0]} con ${empleado_max[1]:,.2f}")
print(f"Empleado que menos gana: {empleado_min[0]} con ${empleado_min[1]:,.2f}")
