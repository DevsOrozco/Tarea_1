"""EJERCICIO 7.- Realiza un programa que pida dos números a y b e indique si su suma es positiva,
negativa o cero."""
print("Ingrese un número:");numero1=float(input())#El usuario ingresa el primer numero
print("Ingrese otro número:");numero2= float(input())#El usuario ingresa el segundi numero

suma=numero1+numero2#Se realiza la suma de los dos numeros
if suma>0:#Si la suma es positiva, se imprime el argumento positivo
    print("La suma es positiva")
elif suma<0:#Si la suma es negativa, se imprime el argumento negativo
    print("La suma es negativa")
else:
    print("La suma es 0")#Caso contrario, se indica que la suma da un valor nulo
