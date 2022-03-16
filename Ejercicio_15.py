"""EJERCICIO 15.
Crea una aplicación que permita adivinar un número."""

print("Por favor, ingrese un número entero en su teclado:")#Se solicita el numero entero al usuario
n1=int(input())#Se almacena el numero en la variable n1
n2=None#Se crea la variable n2 sin un valor
print("*Intenta adivinar el número*")
while n2!=n1:#Mientras el n2 sea distinto a n1, se pide al usuario que intente adivinar el numero
    print("Por favor, ingrese un número por entero en su teclado: ")
    n2=int(input())#El valor ingresado se asigna a n2
    if (n2>n1):#Caso 1: El valor ingresado es mayor al valor de referencia n1, se indica al usuario que ingrese otro valor y se repite el ciclo
        print("El número que insertaste es mayor a", n1, "vuelve a intentarlo.")
    elif (n2<n1):#Caso 2: El valor ingresado es menor al valor de referencia n1, se indica al usuario que ingrese otro valor y se repite el ciclo.
        print("El número que insertaste es menor a", n1, "vuelve a intentarlo.")
    else: #Caso 3: El usuario adivinó el numero, se imprime un mensaje de felicitación.
        print("¡Felicitaciones!, has adivinado el número.\n")

print("*Fin del Juego*")#Fin