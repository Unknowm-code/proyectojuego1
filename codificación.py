#Generador de contraseñas seguras
#Creador: Aaron Gomez 
#Crear contraseñas aleatorias y seguras

import random
import string

#Se define los caracteres que se podrían usar 

#Inlcuye mayusculas y minúsculas
letras = string.ascii_letters 

#Inlcuye del 0 al 9
numeros = string.digits

#Incluye símbolos como @#*!

simbolos = string.punctuation

#combinamos todos los caracteres 

todos = letras + numeros + simbolos

#usamos random para elegir caracteres al azar 

contraseña = '' .join(random.choice(todos) for _ in  range (longit)) return contraseña

# Programa principal
    if longitud
print ("Bienvenido al generador de contraseñas seguras")

#Validamos que es usuario ingrese un numero 

if longitud.isdigit():
longitud = input("¿Cuantos caracteres quieres que tenga tu contraseña? (minimo 8): ")
    longitud = int(longitud)
    if longitud < 8:
        print("La longitud minima recomendada es 8 caracteres.")
    else:
        nueva_contraseña = generar_contraseña(longitud)
        print("\nTu contraseña segura es:")
        print(nueva_contraseña)
    else: 
        print("Por favor, ingresa un numero valido.")