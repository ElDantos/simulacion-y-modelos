'''Juego del dado
   elabodaro por:
   Daniel Silva CI: 27.424.058
   Mariany Bravo CI: 26.469.684'''

from random import randint
import math
''' inicializamos el acumulador y el contador '''
t = 0
acum = 0
''' declaramos el ciclo de las 100 veces en que se va a emular el juego '''
for i in range(100):
    y = 0
    coins = 200
    ''' declaramos el juego con sus 100 iteraciones '''
    while y < 100 and coins > 0 :
        '''lanzamos el dado'''
        dado = randint(1, 6)
        y = y + 1
        '''si el resultado es par ganamos el doble de lo apostado, es decir: 20 monedas'''
        if (math.fmod(dado,2)==0):
            coins = coins + 20
        else:
            ''' si no es par perdemos lo apostado: 10 monedas '''
            coins = coins - 10
    ''' acmulamos las monedas para despues sacar el promedio '''
    acum = acum + coins
    print(f"corridas: {y}, monedas: {coins}")
    ''' contamos las veces en las que nos quedamos sin dinero '''
    if coins <= 0:
        t=t+1

    print("********************************")
    ''' sacamos porcentaje de exito '''
    promedio_exito = 100 - t
    ''' sacamos el promedio de monedas ganadas '''
    promedio_monedas = acum / 100

print(f"final, el porcentaje de exito es de: {promedio_exito}%")
print(f"El promedio total de todo el experimento es de: {promedio_monedas} monedas ganadas. con un inicio de 200 monedas en bolsa")

if promedio_monedas > 200 and promedio_exito > 80:
    print("El juego es rentable")
else:
    print("El juego no es rentable")