"""EJERCICIO 10.
Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y 
“passwd#” se indica “Has entrado al sistema”, sino se da un error."""
for contador in range (1,100):#Uso una funcion for con un contador hasta 100 intentos. 
    print("Ingrese su nombre de usuario:");usuario=str(input())#Se pide al usuario que ingrese su nombre
    print("Ingrese su contraseña: ");clave=str(input())#Se pide al usuario que ingrese su contraseña
    if usuario=="pepe" and clave =="passwd#":#Se compara el string de usuario y clave con los correctos
        print("Hola pepe, has entrado al sistema")#Caso1: El usuario logra ingresar al sistema
        break#Se sale del bucle
    else:
        print("Error, usuario o contraseña inválidos")#Caso 2: El usuario no logra ingresar al sistema, se repite el bucle.
        contador=+1