
#Ejercicio 1

edad = int(input("Ingresa tu edad: "))

if edad > 18:
    print("Es mayor de edad")


#Ejercicio 2

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#Ejercicio 3

num1 = int(input("Ingrese un número par: "))

if (num1 % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#Ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Su categoria es Niño/a")
elif edad >= 12 and edad < 18:
    print("Su categoria es Adolescente")
elif edad >= 18 and edad < 30:
    print("Su categoria es Adulto/a joven")
elif edad >= 30:
    print("Su categoria es Adulto/a")


#Ejercicio 5

contrasena = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

if len(contrasena) >= 8 and len(contrasena) <=14: 
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6

from statistics import mode, median, mean

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("La distribución no se ajusta a los criterios de sesgo definidos")


#Ejercicio 7

palabra = input("Ingrese una palabra o frase: ")

if palabra[-1].lower() == "a" or palabra[-1].lower() == "e" or palabra[-1].lower() == "i" or palabra[-1].lower() == "o" or palabra[-1].lower() == "u":
    palabra = palabra + "!"
    print(palabra)
else:
    print(palabra)


#Ejercicio 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingresá 1, 2 o 3: "))

if opcion == 1: 
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
elif opcion == 3: 
    resultado = nombre.title()
else:
    resultado = "Opción no válida."

print(resultado)


#Ejercicio 9

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")  
elif magnitud >= 7:
    print("Extremo") 


#Ejercicio 10

hemisferio = input("Ingresa en que hemisferio te encuentras (N/S): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el dia (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        estacion = "Primavera"

print(f"La estacion es {estacion}")


















