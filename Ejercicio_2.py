"""EJERCICIO 2.
Calcular el perímetro y área de un círculo dado su radio."""
from math import pi#Se importa la variable predeterminada pi de la biblioteca math

print("Por favor, escriba un valor de radio:")#Se le pide al usuario ingresar un valor de radio
radio=float(input())#El usuario escribe un valor de radio, tipo float
"""print("Por favor, indique las unidades de su radio:")
unidad=str(input())"""
area = pi*radio*radio#Con el valor del radio, se calcula el área del circulo
perimetro = 2*pi*radio#Se caldula el perímetro

print("El valor del perímetro es:",perimetro)#Se muestra el valor del perímetro
print("El valor del área es:",area)#Se muestra el valor del area