"""EJERCICIO 12.
Programa que lea un carácter por teclado y compruebe si es una letra mayúscula."""
#Para este ejercicio necesito importar las bibliotecas de mayúsculas y minúsculas de string
from string import ascii_uppercase
from string import ascii_lowercase
while True:
    print("Escriba una letra en su teclado:")#Se pide al usuario que escriba un caracter en el teclado
    car=str(input())#Se almacena el caracter en la variable car
    if car>='a' and car<='z':#Se compara el número de bits de cada caracter ingresado, si está entre a y z, es minúscula
        print("Es minúscula")
        break
    elif car>="A" and car<="Z":#Se compara el número de bits de cada caracter ingresado, si está entre A y Z, es mayúscula
        print("Es una mayúscula")
        break
    else:
        print("No ingresó una letra")#Se avisa al usuario que no ingresó una letra, el ciclo se repite hasta que ingrese una letra.
