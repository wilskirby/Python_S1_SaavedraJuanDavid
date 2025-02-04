## Ejercicio3 Juan David Saavedra Jaimez C.C 1095798802
print ("Los numeros que aparecen el la sucesion P^3 + Q^4 -2 * P^2 < 680 son: ")
for p in range (0,200):
    for q in range (0,200):
        mat=p**3 + q**4 -2 * p**2
        if(mat<680):
            print ("P: ",p)
            print ("Q: ",q)
            print ("Resultado: ",mat)