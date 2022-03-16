"""EJERCICIO 9.
Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que
tiene el mes correspondiente."""
print("Por favor ingrese un número entre uno y doce:");mes=int(input())#Se pide al usuario que ingrese un numero entero y se almacena en la variable mes
diccionario1={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}#Diccionario con los numeros de los meses y el numero de dias por cada uno
diccionario2={1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}
#Diccionario con los numeros de meses y sus respectivos nombres.
print ("El mes", diccionario2 [mes], "tiene", diccionario1 [mes], "dias")#Se imprime el resultado según el mes indicado por el usuario
