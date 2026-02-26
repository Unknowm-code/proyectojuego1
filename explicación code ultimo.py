importa libreias

random: para genear valores aleatorios
string: contiene conjuntos de caracteres utiles (letras, digitos, simbolos)

lower = string.ascii_lowercase
guarda en la varibale ´lower´ todas las letras minusculas del alfabeto

upper = string.ascii_uppercase
guarda en upper todas las letras mayusculas

num = string.digits
guarda en numeros todos los digitos 

symbols = string.puntuation
guarda en symbols los caracteres de puntuacion y simbolos

chars = lower + upper + num + symbols
une todos los conjuntos anteriores en una sola cadena chars

temp = random.sample(chars, 25)
selecciona 25 caracteres distintos al azar de la cadena chars

print("",join(temp))
une los 25 caracteres seleccionados en una sola cadena (sin espacios ni comas) y la imprime como la contraseña generada