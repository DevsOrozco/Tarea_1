"""EJERCICIO 11.
Escribir un programa que lea un año indicar si es bisiesto. 
Nota: un año es bisiesto si es un número divisible por 4, 
pero no si es divisible por 100, excepto que también sea divisible por 400.""" 

print("Escriba el número de año: ");anio=int(input())#Se pide al usuario que indique un año
if anio%4==0 and anio%400==0 or anio%100!=0:#Se plantea una funcion de 3 condiciones: Si el año es divisible para cuatro y es divisible para 400 o no es divisible para 100.
    print("Año bisiesto")#Impresion de resultados

else:
    print("Año no bisiesto")

