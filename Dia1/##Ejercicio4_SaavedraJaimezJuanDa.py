##Ejercicio 4 Juan David Saavedra Jaimez C.C 1095798802
grande=0
peque=0
for i in range (1,11):
    N=int(input("Ingresa un numer: "))
    if i==1:
        grande=N
        peque=N
    elif N> grande:
        grande=N
    elif N< peque:
        peque=N

print ("El mayor numero es: ",grande)
print ("El menor numero es: ",peque)
