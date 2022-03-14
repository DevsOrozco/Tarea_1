"""EJERCICIO 4.
Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, 
con espacios intermedios."""

print("Por favor, ingrese una palabra: ")#Se pide al usuario que ingrese una palabra
palabra=str(input())#Se almacenan los caracteres en la variable palabra
for contador in range(1,1001):#Se establece una funcion con un contador en el rango de 1 a 1001
    print(contador, palabra)#Mientras contador sea menor a 1001, se imprime el contador y la palabra
