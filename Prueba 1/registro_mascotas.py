nombre = (input("Ingrese el nombre de la mascota: "))
especie = (input("Ingrese la especie de la mascota: "))
edad = (input("Ingrese la edad de la mascota: "))

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre 
        self.especie = especie
        self.edad = edad 

#class Mostrar_informacion:

while True:
    print ("Bienvenido al Registro de Mascotas")
    Mascotas = 0
    Mascotas = int(input("Ingrese la cantidad de Mascotas que desea registrar: "))
    if Mascotas <= 0:
        print("Error: Ingrese un valor valido mayor a 0")
    else : 
        for i in range (Mascotas):
        print




