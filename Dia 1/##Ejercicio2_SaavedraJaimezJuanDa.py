##Ejercicio2 Juan DAvid Saavedra Jaimez C.C 10095798802
UntTerminos=int(input("Ingrese el ultimo numero de la sucesion: "))
if UntTerminos <= 0:
    print ("0")

sum = 0
for i in range (1,UntTerminos):
    if (i%2 == 0):
        sum = sum- (1/i)
    else:
        sum=sum+(1/i)

print ("La cantidad de terminos son: ",UntTerminos)
print ("La sumatoria es: ",sum)