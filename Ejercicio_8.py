"""EJERCICIO 8.  
Escribe un programa que lea un número e indique si es par o impar."""
print("Ingrese un número:");numero=float(input())#Se pide al usuario ingresar un numero
if numero%2==0:#Se evalúa si el módulo del numero es igual a cero (par)
    print("Es par")
elif numero%2!=0:#Se evalúa si el módulo del número es distinto que 0 (impar)
    print("Es impar")