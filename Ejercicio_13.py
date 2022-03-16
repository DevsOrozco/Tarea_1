"""EJERCICIO 13
Pedir un número por teclado y mostrar la tabla de multiplicar"""
print("Por favor ingrese un número entero:")#Se solicita al usuario que ingrese un entero
num=int(input())#Se almacena el entero en la variable num
if num!=0:#Se escribe la condicion, si el numero es distinto de 0, se imprime la tabla de multiplicar
    print("*Tabla de multiplicar del",num,"*")
    contador=0#Se crea un contador, al cual se le asigna el valor de 0
    while contador<=10:#Muentras el contador sea menor o igual a 10
        print(num,"x", contador,"=",num*contador)#Se escribe la operación de multiplicación y su respuesta
        contador+=1#Se suma 1 al contador para pasar al siguiente ciclo
    else: 
        print("Fin de la tabla")