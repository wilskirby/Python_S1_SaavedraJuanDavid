## Ejercicio7 Juan David Saavedra Jaimez C.C 1095798802
n1=int(input("Ingresa n1: " ))
n2=int(input("Ingresa n2: "))
sum1=0
sum2=0
for i in range (1,n1):
    if (n1%i == 0):
        sum1+=i

for i in range (1,n2):
    if (n2%i == 0):
        sum2+=i

if sum1 == n2 and sum2 == n1:
    print("Son numeros amigos")
else:
    print("No son numeros amigos")
