"""EJERCICIO 3
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos"""
print("Por favor, ingrese un número:")#Se pide al usuario que ingrese el primer numero
n1=float(input())
print("Por favor, ingrese otro número:")#Se pide al usuario que ingrese el segundo numero
n2=float(input())

suma=n1+n2#Se almacena la suma de los dos numeros
resta=n1-n2#Se almacena la resta de los dos numeros
mult=n1*n2#Se almacena la multiplicacion de los dos numeros
div=n1/n2#Se almacena la division de los dos numeros

#Se muestran los resultados en pantalla
print("La suma de los numeros es:",suma)
print("La resta de los numeros es:",resta)
print("La multiplicación de los numeros es:",mult)
print("La división de los numeros es:",div)