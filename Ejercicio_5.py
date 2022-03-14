"""EJERCICIO 5.
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla 
cuantas horas y minutos corresponde."""
print("Ingrese una cantidad de minutos: ")#Se pide al usuario que ingrese una cantidad de minutos
minutos=float(input())#Se almacenan los minutos

hora=int(minutos/60)#Se calcula la hora en forma de entero
min=int(((minutos/60)-hora)*60)#Se obtiene el residuo de la division previa y se multiplica por 60

print(minutos,"minutos son:",hora,"horas con",min,"minutos")#Se presentan los resultados