import random

print("=================================")
print("====seleccione un numero=========")
print("=================================")

n = int(input("dijite un numero entre 1 a 100: "))

z  = random.randint(1, 100) #genera un numero entre 1 y 100

i = 1
if n == z:
    r ="ganaste el juego"
else:
    while n < z or n > z:
        i = i + 1 
        if n < z :
            r ="el numero es mas grande"
        else:
            r ="el numero es mas pequeño"
        print(r)
        n = int(input("dijite otro numero "))

print("acertaste a :" + str(i) + " intentos")




