
#Ejercicio 1
print("Hola mundo")

#Ejercicio 2
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
pais = input("Ingresa tu pais: ")
print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {pais}.")

#Ejercicio 4
radio = float(input("Ingrese el radio del circulo: "))

import math

perimetro = math.pi * radio * 2
area = math.pi * radio ** 2

print(f"El area del circulo es de {area} y su perimetro es de {perimetro}")

#Ejercicio 5
segundos = float(input("Ingrese los segundos: "))

horas = segundos / 3600

print(f"Equivale a {horas} horas")

#Ejercicio 6

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Ejercicio 7

numero1 = int(input("Ingrese el primer numero entero, distinto de 0: "))
numero2 = int(input("Ingrese el segundo numero entero, distinto de 0: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2


print(f"La suma es de {suma}")
print(f"La resta es de {resta}")
print(f"La multiplicacion es de {multiplicacion}")
print(f"La division es de {division}")

#Ejercicio 8

altura = float(input("Ingrese su peso: "))
peso = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su IMC es de {imc}")

#Ejercicio 9

gradosCelsius = float(input("Ingrese la temperatura en grados Celsius: "))

gradosFahrenheit = (9 / 5 * gradosCelsius) + 32

print(f"Equivale a {gradosFahrenheit} grados Fahrenheit")

#Ejercicio 10

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio es de {promedio}")


