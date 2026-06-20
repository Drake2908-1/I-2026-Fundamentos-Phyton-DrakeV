import random


letras = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
caracteres = [
    "¡", "!", "¿", "?", ",", ";", ".", ":", "-", "_", "/", "()", "(", ")", "[]", "=", "*" 
]
numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
def contrasena_segura():
    contrasena = " "
    for i in range(4):
        letra = random.choice(letras)
        if i < 2:
            contrasena += letra.upper()
        else:
            contrasena += letra.lower()
    for i in range(4):
        contrasena += random.choice(caracteres)
    for i in range(4):
        contrasena += random.choice(numbers)
    return contrasena

contrasena = contrasena_segura()
print("La nueva contraseña es: ", contrasena)
