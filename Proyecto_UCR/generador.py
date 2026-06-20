import ramdom

letras = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    "A", "B", "C", "D", "C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    ]


def contrasena_segura():
    formato=sting.digits+signos.especiales+numeros.n0
    contrasena = " "
    for i in range (extension):
        contrasena += ramdom.choice(contrasena)
        return contrasena

extension=int(input("Cual es la extensión deseada en la contraseña"))
contrasena_lista = contrasena_segura(extension)
print("La nueva contraseña es:",contrasena_lista)
