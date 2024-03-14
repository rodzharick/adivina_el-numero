# programa para  adivinar un numero entre el 1 y el 10
from random import *

# input
X = int(input("ingrese el numero entre 1,10 : "))

#processing and output
Y = randint (1,10)

if X == Y:
    print("has adivinado el numero",Y,)
elif X>Y:
    print("el numero ingresado ",X,"es mayor al numero a adivinar" ,Y,)
else:
    print(" el numero ingresado ",X," es menor al adivinar",Y,)

